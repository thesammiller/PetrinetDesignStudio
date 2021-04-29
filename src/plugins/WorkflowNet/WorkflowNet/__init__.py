"""
This is where the implementation of the plugin code goes.
The WorkflowNet-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('WorkflowNet')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class WorkflowNet(PluginBase):
    def main(self):
        core = self.core
        root_node = self.root_node
        active_node = self.active_node

    self.testWorkflowNet()
    
  '''
  Workflow Net
  if it has exactly one source place s where *s=∅, 
  one sink place o where o* =∅, 
  and every x∈P∪T is on a path from s to o.
  '''
  def testWorkflowNet(self):
    active_node = self.active_node
    core = self.core
    logger = self.logger
    
    nodes = core.load_sub_tree(active_node)
    path2node = {}
    place = {}
    for node in nodes:
      path2node[core.get_path(node)] = node
      meta_node = core.get_base_type(node)
      meta_type = core.get_attribute(meta_node, "name") 
      if meta_type in ["Place", "Start", "End"]:
        node_data = {}
        node_data['name'] = core.get_attribute(node, "name")
        node_data['children'] = core.get_children_paths(node)
        place[core.get_path(node)] = node_data
        
    inplaces = []
    outplaces = []
    connections = []
    for node in nodes:
      meta_node = core.get_base_type(node)
      connections.append(node)
      meta_type = core.get_attribute(meta_node, "name")
      #logger.info(meta_type)
      if  meta_type in ["ArcPxT"]:
        try:
          #create tuple pairs of src-dst -- these should all be unique
          inplaces.append((core.get_attribute(path2node[core.get_pointer_path(node, 'src')], 'name'), core.get_attribute(path2node[core.get_pointer_path(node, 'dst')], 'name')))    
        except:
          pass
      if  meta_type in ["ArcTxP"]:
        try:
          #create tuple pairs of src-dst -- these should all be unique
          outplaces.append((core.get_attribute(path2node[core.get_pointer_path(node, 'src')], 'name'), core.get_attribute(path2node[core.get_pointer_path(node, 'dst')], 'name')))    
        except:
          pass    
    logger.info(inplaces)
    logger.info(outplaces)
    
    #create pairs of places connected by transitions
    workflow = [[x[0], y[1]] for x in inplaces for y in outplaces if x[1] == y[0]]
    #unnext the places connected
    workflow_data = [y for x in workflow for y in x]
    #create a set of unique locations
    workflow_set = set(workflow_data)
    #create a backup
    workflow_backup = workflow_data[::]
    for s in workflow_set:
      index = workflow_backup.index(s)
      workflow_backup.pop(index)
    workflow_leftovers = [x for x in workflow_set if x not in workflow_backup]
    logger.info(workflow_leftovers)
    
    
    if len(workflow_leftovers) == 2 and workflow_leftovers[0] in [x[0] for x in workflow] and workflow_leftovers[1] in [x[1] for x in workflow]:
        logger.info("THIS IS A WORKFLOW NET.")
    else:
      logger.info("THIS IS NOT A WORKFLOW NET.")
                
    
    
