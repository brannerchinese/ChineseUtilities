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
theHead.appendChild(theTitle);
global.theBody = document.body;
var theHeading = document.createElement('h1');
theHeading.innerHTML=pageName;
global.theBody.appendChild(theHeading);
// 2. Form
global.theForm = document.getElementById('kanjiForm');
global.theBody.appendChild(global.theForm);
// 2a. Form: Search box
var searchBox = document.getElementById('theSearchBox');
searchBox.defaultValue='Enter text here.';
searchBox.onkeydown=clearField;
//global.theForm.appendChild(searchBox);
searchBox.focus();
// 2b. Form: Button
var theButton = document.createElement('button');
global.theForm.appendChild(theButton);
global.theBody.appendChild(global.theForm);
theButton.type='button';
theButton.id='Submit';
theButton.onclick=process1;
theButton.innerHTML='Submit text';
// 3. Table
global.tableBody = document.getElementById('theTable');
var theButton = document.createElement('button');
global.theForm.appendChild(theButton);
global.theBody.appendChild(global.theForm);
global.theBody.appendChild(global.tableBody);


function process1(){
  theLines = parse();
  clearField();
  var newTableBody = rotateTable(theLines);
  replaceTable(newTableBody);
  formatDirection();
}

function process2(){
  var newTableBody = rotateTable(theLines);
  replaceTable(newTableBody);
  formatDirection();
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
    else {global.tableBody.insertBefore(rowArray, newTableBody.firstChild);}
  }
  return newTableBody;
}

function replaceTable(newTableBody) {
  global.theBody.replaceChild(newTableBody, global.tableBody);
  global.tableBody = newTableBody;
  theButton.type='button';
  theButton.id='turnButton';
  theButton.onclick=process2;
//  theButton.innerHTML='Rotate text';
//  global.theBody.appendChild(theButton);
}

function formatDirection(){
  //document.getElementById("theTable")[0].className="vertical"; 
  var buttonText = "Change to columnar text";
  if (global.directionVertical) {
    buttonText = "Change to horizontal text";
    // If Chinese text, we also want lines separated by space, 
    // for clarity as to what a line consists of.
    global.tableBody.className="horizontal";
  }
  else {
    global.tableBody.className="vertical";
  }
  document.getElementById("turnButton").innerHTML=buttonText;
  console.log("direction = vertical?", global.directionVertical);
}                                                                               

function clearField(){
  if (this.defaultValue === this.value) {
    this.value = '';
  }
}

