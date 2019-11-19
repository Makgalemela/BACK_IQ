
   $(document).ready(function() { 
        setInterval('refreshPage()', 60000);
        // console.log("refreshing");
    });
    function refreshPage() { 
        // console.log("refreshed");
        // //location.reload(); 
         $('#container').load('#container');
    };
