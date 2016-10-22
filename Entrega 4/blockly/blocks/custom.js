'use strict';

goog.provide('Blockly.Blocks.custom');

goog.require('Blockly.Blocks');

/*
---------------------------------------------------------
                    Main and Module
    
---------------------------------------------------------
*/
Blockly.Blocks['module'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Module")
        .appendField(new Blockly.FieldTextInput("'id'"), "ID");
    this.appendStatementInput("Input")
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


Blockly.Blocks['function_params'] = {
  init: function() {
    this.appendValueInput("PARAMS")
        .setCheck(null)
        .appendField("func")
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int", "int"], ["float", "float"], ["char", "char"], ["void", "void"]]), "TYPE")
        .appendField(new Blockly.FieldTextInput("id"), "ID");
    this.appendStatementInput("NAME")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['function_without_params'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("func")
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int", "int"], ["float", "float"], ["char", "char"], ["void", "void"]]), "TYPE")
        .appendField(new Blockly.FieldTextInput("id"), "ID");
    this.appendStatementInput("NAME")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['parameter_no_comma'] = {
  init: function() {
    this.appendDummyInput()
         .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int",      "int"], ["float", "float"], ["char", "char"]]), "TYPE")
        .appendField(new Blockly.FieldTextInput("'name'"), "name_param");
    this.setOutput(true, null);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['param_comma'] = {
  init: function() {
    this.appendValueInput("params_with_comma")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int", "int"], ["float", "float"], ["char", "char"]]), "TYPE")
        .appendField(new Blockly.FieldTextInput("' name' "), "name_param");
    this.setOutput(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};




Blockly.Blocks['function_call_params'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("'functionID'"), "FUNCNAME");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['function_call_no_param'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("'functionID'"), "FUNCNAME");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['function_return_params'] = {
  init: function() {
    this.appendValueInput("function")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("func"), "FUNC");
    this.setOutput(true, null);
    this.setColour(330);
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


Blockly.Blocks['variable_definition'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int", "int"], ["char", "char"], ["float", "float"]]), "TYPE")
        .appendField(new Blockly.FieldTextInput("id"), "ID")
        .appendField("=")
        .appendField(new Blockly.FieldTextInput("value"), "VALUE");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};



Blockly.Blocks['variable_with_comma'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int", "int"], ["char", "char"], ["float", "float"]]), "TYPE")
        .appendField(new Blockly.FieldTextInput("id"), "ID")
        .appendField("=")
        .appendField(new Blockly.FieldTextInput("value"), "VALUE");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['variable_comma'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("id"), "ID")
        .appendField("=")
        .appendField(new Blockly.FieldTextInput("value"), "VALUE");
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['variable_comma_end'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("id"), "ID")
        .appendField("=")
        .appendField(new Blockly.FieldTextInput("value"), "VALUE");
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};



Blockly.Blocks['variable_asignation'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("id"), "ID")
        .appendField("=");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};



Blockly.Blocks['id_without_comma'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("'id'"), "ID");
    this.setOutput(true, null);
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['id_with_comma'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("id"), "ID");
    this.setOutput(true, null);
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


/*
---------------------------------------------------------
                        Constants 
    
---------------------------------------------------------
*/


Blockly.Blocks['numerical_const_comma'] = {
  init: function() {
    this.appendValueInput("CONSN")
        .setCheck(null)
        .appendField(new Blockly.FieldNumber(0), "NAME");
    this.setOutput(true, null);
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['numerical_const_no_comma'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldNumber(0), "CONSN");
    this.setOutput(true, null);
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};



/*
---------------------------------------------------------
                        Arrays 
    
---------------------------------------------------------
*/

Blockly.Blocks['array_definition'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int", "int"], ["char", "char"], ["float", "float"]]), "TYPE")
        .appendField(new Blockly.FieldTextInput("id"), "ID")
        .appendField("[")
        .appendField(new Blockly.FieldNumber(0, 1), "SIZE")
        .appendField("]")
        .appendField("=");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(225);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['array_asignation'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("id"), "ID")
        .appendField("[")
        .appendField(new Blockly.FieldNumber(0, 1), "PLACE")
        .appendField("]")
        .appendField("=");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(225);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['array_access'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("id"), "ID")
        .appendField("[")
        .appendField(new Blockly.FieldNumber(0, 1), "SIZE")
        .appendField("]");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(225);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


/*
---------------------------------------------------------
                        I/O 
    
---------------------------------------------------------
*/


Blockly.Blocks['read'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("read")
        .appendField(new Blockly.FieldTextInput("id"), "ID")
        .appendField("=")
        .appendField(new Blockly.FieldTextInput("value"), "VALUE");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(250);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['print'] = {
  init: function() {
    this.appendValueInput("VALUE")
        .setCheck(null)
        .appendField("print");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(250);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


/*
---------------------------------------------------------
                        Operations  
    
---------------------------------------------------------
*/




Blockly.Blocks['parentesis'] = {
  init: function() {
    this.appendValueInput("VALUE")
        .setCheck(null)
        .appendField("(");
    this.appendDummyInput()
        .appendField(")");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setColour(120);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};




