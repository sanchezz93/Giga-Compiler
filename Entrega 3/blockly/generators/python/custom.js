Blockly.Python['module'] = function(block) {
  var value_module_id = Blockly.Python.valueToCode(block, 'MODULE_ID', Blockly.Python.ORDER_ATOMIC);
  var statements_name = Blockly.Python.statementToCode(block, 'NAME');
  // TODO: Assemble Python into code variable.
  var code = '...\n';
  return code;
};