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

    // establish dateValue as a global variable and call it later


    // Need to set it up for when pywebviewready
    // adding table element made it unmodular

    // let dateValue = null

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
            // alert("Building...")

            // const customDateCheck = await window.pywebview.api.checkUserDefaults("Customize Date")
            // alert(customDateCheck.bool)
            // alert("checked")

            // if (customDateCheck.bool === false) {
            //     alert("Would you like to set a custom date?")
                
            //     // selects files AND writes to json
            //     const updateCustomDate = await window.pywebview.api.selectCustomDateFile()
            // customDateStatus.innerHTML = updateCustomDate
            // alert("Custom Date updated")
            // } else {
                // alert("Custom Date found")
            


            const balanceCheck = await window.pywebview.api.checkUserDefaults("Balance")
            // alert(balanceCheck.bool)


            if (balanceCheck.bool === false) {
                alert("Please select a Balance file")
                
                // selects files AND writes to json
                const updateBalance = await window.pywebview.api.selectBalanceFile()
                balanceStatus.innerHTML = updateBalance
                // alert("Balance updated")
            } else {
                // alert("Balance found")
            }


            const scheduleCheck = await window.pywebview.api.checkUserDefaults("Schedules")
            // alert(scheduleCheck.bool)

            if (scheduleCheck.bool === false) {
                alert("Please select a Schedule file")

                // selects files AND writes to json
                const updateSchedule = await window.pywebview.api.selectScheduleFile()
                scheduleStatus.innerHTML = updateSchedule
                // alert(updateSchedule)
            } else {
                // alert("Schedule found")
            }


            const salesCheck = await window.pywebview.api.checkUserDefaults("Sales")
            // alert(salesCheck.bool)

            if (salesCheck.bool === false) {
                alert("Please select a Sales file")
                                
                // selects files AND writes to json
                const updateSales = await window.pywebview.api.selectSalesFile()
                salesStatus.innerHTML = updateSales

                // alert(updateSales)
            } else {
                // alert("Sales found")
            }


            const invoiceCheck = await window.pywebview.api.checkUserDefaults("Invoices")
            // alert(invoiceCheck.bool)

            if (invoiceCheck.bool === false) {
                alert("Please select an Invoice file")

                // selects files AND writes to json
                const updateInvoice = await window.pywebview.api.selectInvoiceFile()
                invoiceStatus.innerHTML = updateInvoice
                
                // alert(updateInvoice)
            } else {
                // alert("Invoices found")
            }


            const hotelCheck = await window.pywebview.api.checkUserDefaults("Hotel - Schedule")
            // alert(hotelCheck.bool)

            if (hotelCheck.bool === false) {
                alert("Please select a Hotel - Schedule file")

                // selects files AND writes to json
                const updateHotel = await window.pywebview.api.selectHotelFile()
                hotelStatus.innerHTML = updateHotel

                // alert(updateHotel)
            } else {
                // alert("Hotel - Schedule found")
            }


            const destCheck = await window.pywebview.api.checkUserDefaults("Destination Folder")
            // alert(destCheck.bool)

            if (destCheck.bool === false) {
                alert("Please select a Destination Folder")

                const updateDest = await window.pywebview.api.selectDestinationFolder()
                destinationStatus.innerHTML = updateDest

                // alert(updateDest)
            } else {
                // alert("Destination Folder found")
            }


            const buildStat = window.pywebview.api.initializeBuildDirectory()

        } catch (error) {

        }
    })
    



    customDate.addEventListener("change", async () => {
        try {
            // alert(customDate.checked)

            customDateChoice = customDate.checked;
            customDateChoiceStr = customDateChoice.toString()

            const customDateSetting = await window.pywebview.api.customizeDate(customDateChoiceStr)

            // alert(customDateSetting.value)
            if (customDateSetting === "true") {
                customDateStatus.innerHTML = customDateTrue
            } else {
                customDateStatus.innerHTML = customDateFalse
            }
            // customDateStatus.innerHTML = customDateSetting.value


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



    // async function check(fileProp, setting) {
    //     return new Promise((resolve, reject) => {
    //         window.addEventListener('pywebviewready', async () => {
    //             try {
    //                 const filePropStatus = await window.pywebview.api.loadUserDefaults(fileProp);
    //                 if (filePropStatus.bool === true) {
    //                     setting.innerHTML = filePropStatus.value;
    //                     resolve(filePropStatus.value);
    //                 } else {
    //                     setting.innerHTML = `❌ ${fileProp} needs to be set`;
    //                     resolve(null);
    //                 }
    //             } catch (err) {
    //                 alert(`Error loading default: ${err}`);
    //                 reject(err);
    //             }
    //         });
    //     });
    // }






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
    progressStatus.innerHTML = value.progressDescription
}

function updateProgress(value){
    progressBar.value = value
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
   