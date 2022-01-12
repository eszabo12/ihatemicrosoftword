
int main(){
    // Load the document from disk.
    System::SharedPtr<Document> doc = System::MakeObject<Document>( u"Word.docx");
    // Set the output PDF path
    System::String outputPath =  u"DOCX-to-PDF.pdf";
    // Convert DOCX to PDF
    doc->Save(outputPath);
    std::cout << "Converted DOCX to PDF successfuly.";
}
