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



Blockly.JavaScript['function_params'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_id = block.getFieldValue('ID');
  var value_params = Blockly.JavaScript.valueToCode(block, 'PARAMS', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_name = Blockly.JavaScript.statementToCode(block, 'NAME');
  // TODO: Assemble JavaScript into code variable.
  value_params = value_params.replace(/[()]/g,'');
  var code = 'func '+ dropdown_type + ' ' + text_id + ' (' + value_params +')' + '{\n' + statements_name + '\n}\n';
  return code;
};



Blockly.JavaScript['function_without_params'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_id = block.getFieldValue('ID');
  var statements_name = Blockly.JavaScript.statementToCode(block, 'NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = 'func '+ dropdown_type + ' ' + text_id +' (){\n' + statements_name + '\n}\n';
  return code;
};


Blockly.JavaScript['parameter_no_comma'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_name_param = block.getFieldValue('name_param');
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_type + ' ' + text_name_param;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};



Blockly.JavaScript['param_comma'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_name_param = block.getFieldValue('name_param');
  var value_params_with_comma = Blockly.JavaScript.valueToCode(block, 'params_with_comma', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_type + ' ' + text_name_param + ', ' +  value_params_with_comma;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};



Blockly.JavaScript['function_call_params'] = function(block) {
  var text_funcname = block.getFieldValue('FUNCNAME');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_funcname + '¿ ' + value_name + ' ?;\n';
  code = code.replace(/[()]/g,'');
  code = code.replace(/[¿]/g,'(');
  code = code.replace(/[?]/g,')');
  return code;
};

// func ();
Blockly.JavaScript['function_call_no_param'] = function(block) {
  var text_funcname = block.getFieldValue('FUNCNAME');
  // TODO: Assemble JavaScript into code variable.
  var code = text_funcname + '();';
  return code;
};


Blockly.JavaScript['function_return_params'] = function(block) {
  var text_func = block.getFieldValue('FUNC');
  var value_function = Blockly.JavaScript.valueToCode(block, 'function', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  value_function = value_function.replace(/[()]/g,'');
  var code = text_func +  '¿' + value_function + '?';
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};




//return value; 
Blockly.JavaScript['return'] = function(block) {
  var value_return = Blockly.JavaScript.valueToCode(block, 'RETURN', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'return ' + value_return + ';\n';
  code = code.replace(/[()]/g,'');
  code = code.replace(/[¿]/g,'(');
  code = code.replace(/[?]/g,')');
  return code;
};

/*
---------------------------------------------------------
                    Variables
    
---------------------------------------------------------
*/

//type variable = n
Blockly.JavaScript['variable_definition'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_id = block.getFieldValue('ID');
  var text_value = block.getFieldValue('VALUE');
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_type + ' ' + text_id + '=' + text_value +';\n';
  return code;
};

//type variable = n, 
//REVISAR
Blockly.JavaScript['variable_with_comma'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_id = block.getFieldValue('ID');
  var text_value = block.getFieldValue('VALUE');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_type + ' ' + text_id + '=' + text_value +',';
  return code;
};


Blockly.JavaScript['variable_comma'] = function(block) {
  var text_id = block.getFieldValue('ID');
  var text_value = block.getFieldValue('VALUE');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_id + '=' + text_value + ',';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};


Blockly.JavaScript['variable_comma_end'] = function(block) {
  var text_id = block.getFieldValue('ID');
  var text_value = block.getFieldValue('VALUE');
  // TODO: Assemble JavaScript into code variable.
  var code = text_id + '=' + text_value + ';\n';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};


Blockly.JavaScript['variable_asignation'] = function(block) {
  var text_id = block.getFieldValue('ID');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_id + '=' + value_name + ';\n';
  code = code.replace(/[()]/g,'');
  code = code.replace(/[¿]/g,'(');
  code = code.replace(/[?]/g,')');
  return code;
};


Blockly.JavaScript['id_without_comma'] = function(block) {
  var text_id = block.getFieldValue('ID');
  // TODO: Assemble JavaScript into code variable.
  var code = text_id;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};


Blockly.JavaScript['id_with_comma'] = function(block) {
  var text_id = block.getFieldValue('ID');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_id + ', ' + value_name;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};



/*
---------------------------------------------------------
                        Constants 
    
---------------------------------------------------------
*/


Blockly.JavaScript['numerical_const_comma'] = function(block) {
  var number_name = block.getFieldValue('NAME');
  var value_consn = Blockly.JavaScript.valueToCode(block, 'CONSN', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = number_name + ', ' +  value_consn;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};



Blockly.JavaScript['numerical_const_no_comma'] = function(block) {
  var number_consn = block.getFieldValue('CONSN');
  // TODO: Assemble JavaScript into code variable.
  var code = number_consn ;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};




/*
---------------------------------------------------------
                        Arrays 
    
---------------------------------------------------------
*/

//type text_id [2] = 
Blockly.JavaScript['array_definition'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_id = block.getFieldValue('ID');
  var number_size = block.getFieldValue('SIZE');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_type +' ' + text_id + '[' + number_size + '] = '+'['+ value_name + '];\n';
  code = code.replace(/[()]/g,'');
  code = code.replace(/[¿]/g,'(');
  code = code.replace(/[?]/g,')');
  return code;
};


Blockly.JavaScript['array_asignation'] = function(block) {
  var text_id = block.getFieldValue('ID');
  var number_place = block.getFieldValue('PLACE');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_id + '[' + number_size + '] = ' + value_name + ';\n';
  return code;
};


Blockly.JavaScript['array_access'] = function(block) {
  var text_id = block.getFieldValue('ID');
  var number_size = block.getFieldValue('SIZE');
  // TODO: Assemble JavaScript into code variable.
  var code = text_id + '[' + number_size + ']';
  return code;
};


/*
---------------------------------------------------------
                        I/O 
    
---------------------------------------------------------
*/


Blockly.JavaScript['read'] = function(block) {
  var text_id = block.getFieldValue('ID');
  var text_value = block.getFieldValue('VALUE');
  // TODO: Assemble JavaScript into code variable.
  var code = 'read (' + (text_id) + ')' + text_value +';\n';
  return code;
};


Blockly.JavaScript['print'] = function(block) {
  var value_value = Blockly.JavaScript.valueToCode(block, 'VALUE', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'print(' + value_value + ');\n';
  return code;
};

/*
---------------------------------------------------------
                        Operations  
    
---------------------------------------------------------
*/



Blockly.JavaScript['parentesis'] = function(block) {
  var value_value = Blockly.JavaScript.valueToCode(block, 'VALUE', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '¿ ' +  value_value + ' ?';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};


