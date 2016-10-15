/*
---------------------------------------------------------
                    Main and Module
    
---------------------------------------------------------
*/
Blockly.JavaScript['module'] = function(block) {
  var text_id = block.getFieldValue('ID');
  var statements_input = Blockly.JavaScript.statementToCode(block, 'Input');
  // TODO: Assemble JavaScript into code variable.
  var code = 'module ' + text_id + ' {\n' + statements_input + '\n}\n';
  return code;
};

Blockly.JavaScript['id_without_coma'] = function(block) {
  var text_id = block.getFieldValue('ID');
  // TODO: Assemble JavaScript into code variable.
  var code = text_id;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};


Blockly.JavaScript['main'] = function(block) {
  var statements_main_method = Blockly.JavaScript.statementToCode(block, 'main_method');
  // TODO: Assemble JavaScript into code variable.
  var code = 'main {\n' + statements_main_method + '\n}\n';
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
  var code = 'func ' + dropdown_type + ' ' + text_id_function + '(' + value_function_part_one + ') {\n' + statements_function_part_two + '\n}\n';
  return code;
};




Blockly.JavaScript['function_with_void'] = function(block) {
  var text_id_function = block.getFieldValue('id_function');
  var value_function_void_one = Blockly.JavaScript.valueToCode(block, 'function_void_one', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_function_void_two = Blockly.JavaScript.statementToCode(block, 'function_void_two');
  // TODO: Assemble JavaScript into code variable.
  var code = 'func void ' + text_id_function + '(' + value_function_void_one + ') {\n' + statements_function_void_two + '\n}\n';
  return code;
};


Blockly.JavaScript['function_parameter'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_name_param = block.getFieldValue('name_param');
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_type + ' ' + text_name_param;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};

Blockly.JavaScript['param_coma'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_name_param = block.getFieldValue('name_param');
  var value_params_with_coma = Blockly.JavaScript.valueToCode(block, 'params_with_coma', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_type + ' ' + text_name_param + ',';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code];//[code, Blockly.JavaScript.ORDER_ATOMIC];
};

Blockly.JavaScript['function_call'] = function(block) {
  var text_func = block.getFieldValue('FUNC');
  var value_call_func = Blockly.JavaScript.valueToCode(block, 'CALL_FUNC', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_func + '(' + value_call_func + ');';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};



Blockly.JavaScript['return'] = function(block) {
  var value_return = Blockly.JavaScript.valueToCode(block, 'RETURN', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'return ' + value_return + ';\n';
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




