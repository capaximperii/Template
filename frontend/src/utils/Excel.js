import XLSX from "xlsx";

export default class Excel {
  constructor() {
    this.workbook = XLSX.utils.book_new();
  }

  str2ab(s) {
    var buf = new ArrayBuffer(s.length);
    var view = new Uint8Array(buf);
    for (var i = 0; i !== s.length; ++i) view[i] = s.charCodeAt(i) & 0xff;
    return buf;
  }

  // Create a worksheet with data and add it to the workbook
  AddWorkSheetToBook(data, sheetName) {
    let workSheet = XLSX.utils.json_to_sheet(data);
    XLSX.utils.book_append_sheet(this.workbook, workSheet, sheetName);
  }

  // Return a blob of workbook
  Get() {
    let bin = XLSX.write(this.workbook, { bookType: "xlsx", type: "binary" });
    let blob = new Blob([this.str2ab(bin)], {
      type: "application/octet-stream"
    });
    return blob;
  }

  // Popup the save as dialog
  SaveAs(filename) {
    const e = document.createEvent("MouseEvents");
    const a = document.createElement("a");
    a.download = filename;
    a.href = window.URL.createObjectURL(this.Get());
    a.dataset.downloadurl = [
      "application/vnd.ms-excel",
      a.download,
      a.href
    ].join(":");
    e.initEvent(
      "click",
      true,
      false,
      window,
      0,
      0,
      0,
      0,
      0,
      false,
      false,
      false,
      false,
      0,
      null
    );
    a.dispatchEvent(e);
  }
}
