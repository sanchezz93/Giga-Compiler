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