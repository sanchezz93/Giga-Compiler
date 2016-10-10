/*
---------------------------------------------------------
                    Main and Module
    
---------------------------------------------------------
*/
Blockly.Python['module'] = function(block) {
  var value_module_id = Blockly.Python.valueToCode(block, 'MODULE_ID', Blockly.Python.ORDER_ATOMIC);
  var statements_name = Blockly.Python.statementToCode(block, 'NAME');
  // TODO: Assemble Python into code variable.
  var code = '...\n';
  return code;
};


Blockly.Python['main'] = function(block) {
  var statements_main_method = Blockly.Python.statementToCode(block, 'main_method');
  // TODO: Assemble Python into code variable.
  var code = '...\n';
  return code;
};

/*
---------------------------------------------------------
    
                   Functions 
---------------------------------------------------------
*/


Blockly.Python['function_with_type'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_id_function = block.getFieldValue('id_function');
  var value_function_part_one = Blockly.Python.valueToCode(block, 'function_part_one', Blockly.Python.ORDER_ATOMIC);
  var statements_function_part_two = Blockly.Python.statementToCode(block, 'function_part_two');
  // TODO: Assemble Python into code variable.
  var code = '...\n';
  return code;
};



Blockly.Python['function_with_void'] = function(block) {
  var text_id_function = block.getFieldValue('id_function');
  var value_function_void_one = Blockly.Python.valueToCode(block, 'function_void_one', Blockly.Python.ORDER_ATOMIC);
  var statements_function_void_two = Blockly.Python.statementToCode(block, 'function_void_two');
  // TODO: Assemble Python into code variable.
  var code = '...\n';
  return code;
};


Blockly.Python['function_parameter'] = function(block) {
  var text_name_param = block.getFieldValue('name_param');
  var dropdown_type = block.getFieldValue('TYPE');
  // TODO: Assemble Python into code variable.
  var code = '...';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Python['param_coma'] = function(block) {
  var text_name_param = block.getFieldValue('name_param');
  var dropdown_type = block.getFieldValue('TYPE');
  var value_params_with_coma = Blockly.Python.valueToCode(block, 'params_with_coma', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = '...';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['function_call'] = function(block) {
  var text_func = block.getFieldValue('FUNC');
  var value_call_func = Blockly.Python.valueToCode(block, 'CALL_FUNC', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = '...';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Python['return'] = function(block) {
  var value_return = Blockly.Python.valueToCode(block, 'RETURN', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = '...\n';
  return code;
};


/*
---------------------------------------------------------
                    Variables
    
---------------------------------------------------------
*/


Blockly.Python['variable_without_coma'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_name_variable = block.getFieldValue('NAME_VARIABLE');
  // TODO: Assemble Python into code variable.
  var code = '...';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};



Blockly.Python['variable_with_coma'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var dropdown_type = block.getFieldValue('TYPE');
  var value_variables_with_coma = Blockly.Python.valueToCode(block, 'variables_with_coma', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = '...\n';
  return code;
};

