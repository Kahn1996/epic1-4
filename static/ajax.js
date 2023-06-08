$.ajax

http://localhost:5000/create-package
({


    type: "POST",
    data: JSON.stringify(packageData),
    contentType: "application/json",
    success: function(response) {
        console.log(response);
        alert("Package created successfully!");
    },
    error: function(error) {
        console.log(error);
        alert("Error creating package. Please try again.");
    }
});