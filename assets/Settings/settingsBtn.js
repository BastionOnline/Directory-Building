propSettings.addEventListener("click", () => {
    // alert("click")
    if (configTable.style.display === "none" || configTable.style.display === "") {
        configTable.style.display = "table"
    } else {
        configTable.style.display = ""
    }
}  )