/*
---------------------------------------------------------
                    Main and Module
    
---------------------------------------------------------
*/
Blockly.JavaScript['module'] = function(block) {
  var text_id = block.getFieldValue('ID');
  var statements_input = Blockly.JavaScript.statementToCode(block, 'Input');
  // TODO: Assemble JavaScript into code variable.
  var code = 'module'+ statements_input + '{\n}';
  return code;
};

Blockly.JavaScript['id_without_coma'] = function(block) {
  var text_id = block.getFieldValue('ID');
  // TODO: Assemble JavaScript into code variable.
  var code = text_id;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};


Blockly.JavaScript['main'] = function(block) {
  var statements_main_method = Blockly.JavaScript.statementToCode(block, 'main_method');
  // TODO: Assemble JavaScript into code variable.
  var code = 'main {\n}';
  return code;
};

/*
---------------------------------------------------------
    
                   Functions 
---------------------------------------------------------
*/



Blockly.JavaScript['function_with_type'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_id_function = block.getFieldValue('id_function');
  var value_function_part_one = Blockly.JavaScript.valueToCode(block, 'function_part_one', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_function_part_two = Blockly.JavaScript.statementToCode(block, 'function_part_two');
  // TODO: Assemble JavaScript into code variable.
  var code = '...;\n';
  return code;
};




Blockly.JavaScript['function_with_void'] = function(block) {
  var text_id_function = block.getFieldValue('id_function');
  var value_function_void_one = Blockly.JavaScript.valueToCode(block, 'function_void_one', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_function_void_two = Blockly.JavaScript.statementToCode(block, 'function_void_two');
  // TODO: Assemble JavaScript into code variable.
  var code = '...;\n';
  return code;
};


Blockly.JavaScript['function_parameter'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_name_param = block.getFieldValue('name_param');
  // TODO: Assemble JavaScript into code variable.
  var code = '...';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['param_coma'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_name_param = block.getFieldValue('name_param');
  var value_params_with_coma = Blockly.JavaScript.valueToCode(block, 'params_with_coma', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '...';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['function_call'] = function(block) {
  var text_func = block.getFieldValue('FUNC');
  var value_call_func = Blockly.JavaScript.valueToCode(block, 'CALL_FUNC', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '...';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};



Blockly.JavaScript['return'] = function(block) {
  var value_return = Blockly.JavaScript.valueToCode(block, 'RETURN', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '...;\n';
  return code;
};

/*
---------------------------------------------------------
                    Variables
    
---------------------------------------------------------
*/

Blockly.JavaScript['variable_without_coma'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_varname = block.getFieldValue('VARNAME');
  var text_value = block.getFieldValue('VALUE');
  // TODO: Assemble JavaScript into code variable.
  var code = '...;\n';
  return code;
};



Blockly.JavaScript['variable_with_coma'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_varname = block.getFieldValue('VARNAME');
  var text_value = block.getFieldValue('VALUE');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '...;\n';
  return code;
};




