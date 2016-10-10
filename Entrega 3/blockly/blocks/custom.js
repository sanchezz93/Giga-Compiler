'use strict';

/*
---------------------------------------------------------
                    Main and Module
    
---------------------------------------------------------
*/
Blockly.Blocks['module'] = {
  init: function() {
    this.appendValueInput("MODULE_ID")
        .setCheck("String")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("module");
    this.appendStatementInput("NAME")
        .setCheck(["main", "vars", "funcs"]);
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['main'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Main");
    this.appendStatementInput("main_method")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

/*
---------------------------------------------------------
    
                   Functions 
---------------------------------------------------------
*/


Blockly.Blocks['function_with_type'] = {
  init: function() {
    this.appendValueInput("function_part_one")
        .setCheck(null)
        .appendField("function")
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int ", "int"], ["float", "float"], ["char", "char"]]), "TYPE")
        .appendField(new Blockly.FieldTextInput("'id'"), "id_function");
    this.appendStatementInput("function_part_two")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(285);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['function_with_void'] = {
  init: function() {
    this.appendValueInput("function_void_one")
        .setCheck(null)
        .appendField("function")
        .appendField("void")
        .appendField(new Blockly.FieldTextInput("'id'"), "id_function");
    this.appendStatementInput("function_void_two")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(285);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['function_parameter'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("'name'"), "name_param")
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int", "int"], ["float", "float"], ["char", "char"]]), "TYPE");
    this.setOutput(true, null);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['param_coma'] = {
  init: function() {
    this.appendValueInput("params_with_coma")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("' name' "), "name_param")
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int", "int"], ["float", "float"], ["char", "char"]]), "TYPE");
    this.setOutput(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['function_call'] = {
  init: function() {
    this.appendValueInput("CALL_FUNC")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("'id'"), "FUNC");
    this.setOutput(true, null);
    this.setColour(255);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};



Blockly.Blocks['return'] = {
  init: function() {
    this.appendValueInput("RETURN")
        .setCheck(null)
        .appendField("Return");
    this.setPreviousStatement(true, null);
    this.setColour(255);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


/*
---------------------------------------------------------
                    Variables
    
---------------------------------------------------------
*/

Blockly.Blocks['variable_without_coma'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int", "int"], ["float", "float"], ["char", "char"]]), "TYPE")
        .appendField(new Blockly.FieldTextInput("'name'"), "NAME_VARIABLE");
    this.setOutput(true, null);
    this.setColour(180);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};



Blockly.Blocks['variable_with_coma'] = {
  init: function() {
    this.appendValueInput("variables_with_coma")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("'name'"), "VAR")
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int", "int"], ["float", "float"], ["char", "char"]]), "TYPE");
    this.setPreviousStatement(true, null);
    this.setColour(180);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

