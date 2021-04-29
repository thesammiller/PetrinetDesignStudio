"""
This is where the implementation of the plugin code goes.
The FreeChoice-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('FreeChoice')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class FreeChoice(PluginBase):
    def main(self):
        core = self.core
        root_node = self.root_node
        active_node = self.active_node

    self.testFreeChoice()

  '''
  Free-choice petri net - 
    if the intersection of the inplaces sets 
    of two transitions are not empty, 
    then the two transitions should be the same 
    (or in short, each transition has its own unique set of inplaces)
  '''
  def testFreeChoice(self):
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
        
    transitions = []
    connections = []
    for node in nodes:
      meta_node = core.get_base_type(node)
      connections.append(node)
      meta_type = core.get_attribute(meta_node, "name")
      # logger.info(meta_type)
      if  meta_type == "ArcPxT":
        try:
          # create tuple pairs of src-dst -- these should all be unique
          transitions.append((core.get_attribute(path2node[core.get_pointer_path(node, 'src')], 'name'), core.get_attribute(path2node[core.get_pointer_path(node, 'dst')], 'name')))    
        except:
          pass
    if len(transitions) == len(set(transitions)):
      logger.info("THIS IS A FREE CHOICE PETRINET.")
    else:
      logger.info("THIS IS NOT A FREE CHOICE PETRINET.")
