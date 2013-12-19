// rotate_table.js
// 20130611, works
// David Prager Branner
// Given an HTML table of arbitrary size but no merged cells, 
//   flip along the top-left to bottom right diagonal, so that
//   horizontal Chinese text becomes vertical and vice versa.

var global = this;
global.directionVertical = false;
window.onload = reportDirection;

function reportDirection(){
  document.getElementById("theTable").className="vertical";
  var buttonText = "Change to columnar text";
  if (global.directionVertical) {
    buttonText = "Change to horizontal text";
    // If Chinese text, we also want lines separated by space, 
    // for clarity as to what a line consists of.
    document.getElementById("theTable").className="horizontal";
  }
  document.getElementById("turnButton").innerHTML=buttonText;
  console.log("direction = vertical?", global.directionVertical);
}

function turn(){
  global.directionVertical = !global.directionVertical;
  reportDirection();
  var tableBody = document.getElementsByTagName('tbody')[0];
  var rowArray = tableBody.getElementsByTagName('tr');
  var columns= rowArray.length;
  var rows= rowArray[0].getElementsByTagName('td').length;
  var tempTableBody= document.createElement('tbody');
  for (row=0 ; row<rows ; row++){
    tempRow = document.createElement('tr');
    for (column=0 ; column<columns ; column++){
      if (global.directionVertical){index = columns-column-1;}
      else {index = column;}
      nextCell = rowArray[index].getElementsByTagName('td')[0];
      tempRow.appendChild(nextCell);
    }
    if (global.directionVertical) {tempTableBody.appendChild(tempRow);}
    else {tempTableBody.insertBefore(tempRow, tempTableBody.firstChild);}
  }
  tableBody.parentNode.replaceChild(tempTableBody, tableBody);
}
