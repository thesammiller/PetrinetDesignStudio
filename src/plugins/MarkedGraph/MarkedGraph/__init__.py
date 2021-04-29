"""
This is where the implementation of the plugin code goes.
The MarkedGraph-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('MarkedGraph')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class MarkedGraph(PluginBase):
    def main(self):
        core = self.core
        root_node = self.root_node
        active_node = self.active_node

        self.testMarkedGraph()
    
    def testMarkedGraph(self):
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

        check_inplaces = [i[0] for i in inplaces]
        check_outplaces = [o[1] for o in outplaces]
        if len(check_inplaces) == len(set(check_inplaces)) and len(check_outplaces) == len(set(check_outplaces)):
            logger.info("THIS IS A MARKED GRAPH.")
        else:
            logger.info("THIS IS NOT A MARKED GRAPH.")


