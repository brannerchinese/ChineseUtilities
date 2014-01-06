// Filename: tablize_input_kanji.js
// Author: David Prager Branner
// Date: 20130620, in progress
//
// User can enter Chinese text (we assume poem of equal line-length).
// Format as HTML table with option to rotate 90 degrees clockwise.
// Later: under (to right of) each character will be looked-up information
//     (prosodic symbols, readings, etc.)

// Declarations
var global = this;
global.directionVertical = false;
// Pattern for splitting at punctuation. Note that half-commas are a problem.
global.lineSeparators = /[﹅﹆､、]|[\n]|[⸰｡。\.]|[︓：\:]|[︔；\;]|[︕！﹗\!]|[，\,．／]|[？︖\?]|[･・]/; // To do: more will be needed here.
// Pattern for stripping "openers" and "closers" (quotes, brackets, etc.)
global.openClosers = /["“”„‛‟'‘’‚⸢⸣⸤⸥「」｢｣『』〝〞〟]|[()⁽⁾₍₎❨❩❪❫﹙﹚（）｟｠⟮⟯⸨⸩︵︶]|[<>⟨⟩⟪⟫〈〉❬❭❮❯❰❱〈〉《》‹›«»]|[\[\]⟦⟧［］﹇﹈【】︻︼〖〗〚〛❲❳]|[〔〕⦗⦘〘〙﹝﹞︗︘︹︺]|[{}❴❵﹛﹜｛｝︷︸]/g; // I think this is all of consequence.

// Initialize page
// 1. Headings
var pageName = 'play: make table of input kanji';
var theHead = document.head;
var theTitle = document.createElement('title');
theTitle.innerHTML=pageName;
document.head.appendChild(theTitle);
global.theBody = document.body;
var theHeading = document.getElementsByTagName('h1')[0];
theHeading.innerHTML=pageName;
// 2. Form
global.theForm = document.getElementById('container');
// 2a. Form: Search box
var searchBox = document.getElementById('theSearchBox');
searchBox.defaultValue='Enter text here.';
searchBox.onkeydown=clearField;
searchBox.focus();
// 2b. Form: Buttons
global.theButtonPanel = document.getElementById('buttonPanel');
global.inputButton = document.createElement('button');
global.theButtonPanel.appendChild(global.inputButton);
global.inputButton.type='button';
global.inputButton.id='Submit';
global.inputButton.onclick=process1;
global.inputButton.innerHTML='Submit text';
// 3. Table
global.theTable = document.getElementById('theTable');
global.theTableBody = document.getElementById('theTableBody');
nullTable = document.createElement('tr');
global.theTableBody.appendChild(nullTable);
window.alert('end');

function process1(){
  //clearField();
  global.theLines = parse();
  global.turnButton = document.createElement('button');
  global.turnButton.id='turnButton';
  global.turnButton.onclick=process2;
  global.theButtonPanel.appendChild(global.turnButton);
  process2();
}

function process2(){
  var newTableBody = rotateTable(global.theLines);
  // second time around, rotateTable incorrectly rotates table
  // second time around, replaceTable destroys table
  replaceTable(newTableBody);
  formatDirection();
  window.alert('end of process2');
}

function parse(){
  // In:  Contents of searchBox
  // Out: List of lists, one kanji per index, cleaned of punctuation and split
  //      at \n or stop characters.
  lines = searchBox.value.split(global.lineSeparators);
  longestLength = 0;
  allLinesSameLength = null;
  for (i=0 ; i<lines.length ; i++){
    lines[i] = lines[i].replace(global.openClosers, '');
    lines[i] = lines[i].replace(/\s/, '');
    lines[i] = lines[i].toArrayOfUChars();
    // To do: for separate treatment, lines may be prefixed
    //    t: title; also vertical but mark somehow
    //    a: author; also vertical but mark somehow
    //    n: notes to preceding line; must decide how to treat
    //    blank line: respect, allow null; don't new poem w/o title
    // To do: make sure all lines are equal-length; 
    //    if not, at least report length of longest
  }
  return lines;
}

function rotateTable(lines){
  // In:  Array of lines
  // Out: newTableBody: rotated table
  global.directionVertical = !global.directionVertical;
  var newTableBody = document.createElement('table'),
      nextCell = null,
      // columns here means: future number of columns; present number of lines.
      columns = lines.length,
      // rows here means: future number of rows; present number of char/line.
      rows = lines[0].length;
  for (row=0 ; row<rows ; row++){
    rowArray = document.createElement('tr');
    for (column=0 ; column<columns ; column++){
      // Using "index" instead of "column"; allows same code regardless of
      // text's orientation.
      if (global.directionVertical){index = (columns-1) - column;}
      else {index = column;}
      nextCell = document.createElement('td');
      //
      // Preserve blank lines in the original by adding ideographic space.
      if (lines[index] == null){toAdd = '\u3000';}
      else {toAdd = lines[index][row];}
      nextCell.innerHTML = toAdd;
      //
      rowArray.appendChild(nextCell);
    }
    if (global.directionVertical) {newTableBody.appendChild(rowArray);}
    else {global.theTable.insertBefore(rowArray, newTableBody.firstChild);}
  }
  return newTableBody;
}

function replaceTable(newTableBody) {
  global.theTable.replaceChild(newTableBody, global.theTableBody);
  global.theTableBody = newTableBody;
}

function formatDirection(){
  var buttonText = "Change to columnar text";
  if (global.directionVertical) {
    buttonText = "Change to horizontal text";
    // If Chinese text, we also want lines separated by space, 
    // for clarity as to what a line consists of.
    global.theTableBody.className="horizontal";
  }
  else {
    global.theTableBody.className="vertical";
  }
  global.turnButton.innerHTML=buttonText;
  console.log("direction = vertical?", global.directionVertical);
}                                                                               

function clearField(){
  if (this.defaultValue === this.value) {
    this.value = '';
  }
}

