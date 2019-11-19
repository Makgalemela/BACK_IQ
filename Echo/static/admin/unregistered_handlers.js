
$(function () {
  $('.DeviceSelecter').click(function() {   
 
 	$.ajax({
 			async: false,
 			type: 'GET',
 			url : "https://iqmediaapp.herokuapp.com/api/"+$(this).attr('data-id'),
 			datatype : "json",
 			success : function(data , response){
 				var date_ = data.date.substring(0, 10) +"  " +data.date.substring(11, 19);
 				$("#deviceNumber").text("Device ID: "+ data.deviceNumber);
 				$("#Registration").text("Registration Number: "+ data.carRegNumber);
				$("#Owner").text("Car Owner: 	" + data.carOwner);
				$("#Driver").text("Car Driver: 	"+ data.carDriver);
				$("#Model").text("Car Model: "+  data.carModel);
				$("#Status").text("Status: 	"+  data.activeFlag);
  				$("#lastknown").text("Last Known Loc:  "+  data.lastknown);
 				$("#Date").text("Date:    "+ date_ );
 			},
 			 error: function () {
       			 console.log("error");
    		}
  
 		});
 		
    });
})