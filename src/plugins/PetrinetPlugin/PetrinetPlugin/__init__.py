"""
This is where the implementation of the plugin code goes.
The PetrinetPlugin-class is imported from both run_plugin.py and run_debug.py
"""
import json
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('PetrinetPlugin')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class PetrinetPlugin(PluginBase):
  def main(self):
    active_node = self.active_node
    core = self.core
    logger = self.logger

    #logger.info("{}".format(dir(core)))

    data = {}
    
    def at_node(node):
      node_data = {}
      meta_node = core.get_base_type(node)
      node_data['name'] = core.get_attribute(node, 'name')
      node_data['meta_type'] = 'undefined'
      if meta_node:
        node_data['meta_type'] = core.get_attribute(meta_node, 'name')
      node_data['guid'] = core.get_guid(node)
      attrs = {}
      for attr in core.get_attribute_names(node):
        if attr != "pythonCode":
          attrs[attr] = core.get_attribute(node, attr)
      node_data['attributes'] = attrs
      path = core.get_path(node)
      data[path] = node_data

    self.util.traverse(active_node, at_node)

    myData = {}
    
    for key in data:
      #logger.info("-"*32)
      #logger.info("Data for path {key}".format(key=key))
      myData[key] = []
      for attribute in data[key]:
        val = data[key][attribute]
        myData[key].append(attribute)
        if attribute == "attributes" and val != {}:
          #logger.info("\tattributes: ")
          for k in val:
            pass #logger.info("\t\t{attr}:\t{value}".format(attr=k, value=val[k]))
          continue
        elif attribute == "attributes":
          continue
        #logger.info("\t{attr}:\t{value}".format(attr=attribute, value=val))
        # no-op to create time separation for printing
        #for i in range(10**6): pass

    #myData = {key.decode('utf-8'): value for key, value in data.items()}
    myData = {'a': 1, 'b': 2}
    #logger.info(myData)
    dump_data = json.dumps(myData)
    logger.info(dump_data)
    file_hash = self.add_file('Petrinet_Data.txt', dump_data)        
