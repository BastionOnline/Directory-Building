let openBuildLocationBtn = null;
let progressPercentStatus = null;

document.addEventListener("DOMContentLoaded", async () => {
    const balanceBtn = document.getElementById("balanceFileInput")
    const scheduleBtn = document.getElementById("scheduleFileInput")
    const saleBtn = document.getElementById("saleFileInput")
    const invoiceBtn = document.getElementById("invoiceFileInput")
    const destinationFolderBtn = document.getElementById("destinationFolderInput")
    const hotelBtn = document.getElementById("hotelFileInput")    
    const dateInput = document.getElementById("dateInput")
    const customDate = document.getElementById("customDate")
    const progressBar = document.getElementById("progressBar")
    const propSettings = document.getElementById("propSettings")
    const configTable = document.getElementById("configTable")
    const buildBtn = document.getElementById("build")
    openBuildLocationBtn = document.getElementById("openBuildLocation")
    progressPercentStatus = document.getElementById("progressPercentStatus")

    const customDateStatus = document.getElementById("customDateStatus")
    const progressStatus = document.getElementById("progressStatus")
    const balanceStatus = document.getElementById("balanceStatus")
    const scheduleStatus = document.getElementById("scheduleStatus")
    const salesStatus = document.getElementById("salesStatus")
    const invoiceStatus = document.getElementById("invoiceStatus")
    const hotelStatus = document.getElementById("hotelStatus")
    const destinationStatus = document.getElementById("destinationStatus")
    
    customDateTrue = "✅ Custom Date will be set"
    customDateFalse = "❌ Custom Date will not be set"

    propSettings.addEventListener("click", () => {
        // alert("click")
        if (configTable.style.display === "none" || configTable.style.display === "") {
            configTable.style.display = "table"
        } else {
            configTable.style.display = ""
        }
    }  )

    // Need to set it up for when pywebviewready
    // adding table element made it unmodular

    dateInput.addEventListener("change", async () => {
        try{
            // event listener works on html elements not strings or values
            const dateValue = dateInput.value // or valueAsDate
            // alert(dateValue)
            const dateSet = await window.pywebview.api.dateSelection(dateValue)
            
            
        } catch (err) {
            alert("year selection error: ", err);
        }
    })

    // dateInput.addEventListener("wheel", async (event) => {
    //     event.preventDefault();

    //     currentvalue = parseInt(dateInput.value);
        
    //     if (event.deltaY < 0) {
    //         dateInput.value = currentvalue + 1;
    //         await window.pywebview.api.dateSelection(dateInput.value)

    //     } else {
    //         dateInput.value = currentvalue - 1;
    //         await window.pywebview.api.dateSelection(dateInput.value)
    //     }
    // })


    buildBtn.addEventListener("click", async() => {
        try {

            const fileConfig = [
            {
                name: "Balance",
                selectMethod: "selectBalanceFile",
                statusElement: balanceStatus
            },
            {
                name: "Schedules",
                selectMethod: "selectScheduleFile",
                statusElement: scheduleStatus
            },
            {
                name: "Sales",
                selectMethod: "selectSalesFile",
                statusElement: salesStatus
            },
            {
                name: "Invoices",
                selectMethod: "selectInvoiceFile",
                statusElement: invoiceStatus
            },
            {
                name: "Hotel - Schedule",
                selectMethod: "selectHotelFile",
                statusElement: hotelStatus
            },
            {
                name: "Destination Folder",
                selectMethod: "selectDestinationFolder",
                statusElement: destinationStatus
            }
            ];

            for (const item of fileConfig) {
                const checkResult = await window.pywebview.api.checkUserDefaults(item.name);

                if (checkResult.bool === false) {
                    alert(`Please select a ${item.name} file`);

                    // dynamically call the API method using bracket notation
                    const updatedValue = await window.pywebview.api[item.selectMethod]();

                    // update DOM
                    item.statusElement.innerHTML = updatedValue;
                } else {
                    console.log(`${item.name} found`);
                }
            }

        // After all checks, initialize build directory
        await window.pywebview.api.initializeBuildDirectory();

        } catch (error) {

        }
    })
    

    openBuildLocationBtn.addEventListener("click", async () => {
        await window.pywebview.api.openBuildLocation()
    })

    customDate.addEventListener("change", async () => {
        try {
            // alert(customDate.checked)

            customDateChoice = customDate.checked;
            customDateChoiceStr = customDateChoice.toString()

            const customDateSetting = await window.pywebview.api.customizeDate(customDateChoiceStr)

            if (customDateSetting === "true") {
                customDateStatus.innerHTML = customDateTrue
            } else {
                customDateStatus.innerHTML = customDateFalse
            }
        } catch (err) {

        }
    })
        
    balanceBtn.addEventListener("click", async () => {
        try{
            const balanceFilePath = await window.pywebview.api.selectBalanceFile()
            // alert(balanceFilePath)
            balanceStatus.innerHTML = balanceFilePath

            // if (!balanceFilePath) {
            //     alert("Balance File not selected")
            // } else {
            //     alert("Balance File Selected")
            // }
        } catch (err) {
            alert("File selection failed:", err);
            // status.textContent = "❌ File selection failed.";
        }})

    scheduleBtn.addEventListener("click", async () => {
        try {
            const scheduleSetting = await window.pywebview.api.selectScheduleFile()
            // alert(scheduleSetting)
            scheduleStatus.innerHTML = scheduleSetting
        } catch (error) {

        }
    })

    saleBtn.addEventListener("click", async () => {
        try {
            const saleSetting = await window.pywebview.api.selectSalesFile()
            // alert(saleSetting)
            salesStatus.innerHTML = saleSetting
        } catch {

        }
    })

    invoiceBtn.addEventListener("click", async () => {
        try {
            const invoiceSetting = await window.pywebview.api.selectInvoiceFile()
            // alert(invoiceSetting)
            invoiceStatus.innerHTML = invoiceSetting
        } catch {

        }
    })    


    hotelBtn.addEventListener("click", async () => {
        try {
            const hotelSetting = await window.pywebview.api.selectHotelFile()
            // alert(hotelSetting)
            hotelStatus.innerHTML = hotelSetting
        } catch {

        }
    })

    destinationFolderBtn.addEventListener("click", async () => {
        try {
            const destinationSetting = await window.pywebview.api.selectDestinationFolder()
            // alert(destinationSetting)
            destinationStatus.innerHTML = destinationSetting
        } catch {

        }
    })    


    async function check(fileProp, setting) {
        window.addEventListener('pywebviewready', async () => {
            try {
                const filePropStatus = await window.pywebview.api.loadUserDefaults(fileProp);
                // alert(filePropStatus)
                if (filePropStatus.bool === true) {
                    // alert(`${fileProp} found`)
                        if (fileProp === "Customize Date") {
                            if (filePropStatus.value === "true") {
                                filePropStatus.value = customDateTrue
                                customDate.checked = true;
                            }}
                        else if (fileProp === "Year") {
                            // alert(`setting ${fileProp}`)
                            setting.value = filePropStatus.value
                        }
                        setting.innerHTML = filePropStatus.value

                    return "filePropStatus"

                } else {
                    if (fileProp === "Customize Date") {
                        setting.innerHTML = `❌ ${fileProp} will not be set`
                        return "filePropStatus"
                    }
                    setting.innerHTML = `❌ ${fileProp} needs to be set`
                    return "filePropStatus"
                }
            } catch (err) {
                alert(`Error loading default: ${err}`);
                // create needed key, value pair
            }
        })
    }

    check("Year", dateInput)
    check("Customize Date", customDateStatus)
    check("Balance", balanceStatus)
    check("Schedules", scheduleStatus)
    check("Sales", salesStatus)
    check("Invoices", invoiceStatus)
    check("Hotel - Schedule", hotelStatus)
    check("Destination Folder", destinationStatus)




})

// Functions callable from Python
// These functions are called from Python using window.evaluate_js('functionName(args)')    

function handleProgress(data){
    progressBar.value = data.progressValue
    progressStatus.innerHTML = data.progressDescription
    progressPercentStatus.innerHTML = data.progressPercentStatus

    if (data.progressItem == "Completed"){

        openBuildLocationBtn.style.display = "inline"
        // openBuildLocationBtn.value = data.progressLocation
    } else {
        openBuildLocationBtn.style.display = "none"
    }
}

function updateProgress(value){
    progressBar.value = value
    // if (value == 100)
}

function progressStatusUpdate(value){
    progressStatus.innerHTML = value

}

function alertTest(test){
    alert(test)
}

function ring(){
    alert("ring")
}
   