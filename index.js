// Initialize the EPUB book
var book = ePub("./myEpub.epub");

var rendition = book.renderTo("viewer", { method: "continuous", width: "100%", height: "100%" });
var displayed = rendition.display();