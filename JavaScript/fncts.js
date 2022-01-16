  var url="";

  var urlStart="https://relay.amazon.com/api/tours/loadboard?sortByField=creationTime&sortOrder=desc";

  var urlBody="";

  var urlFoot="&equipmentTypeFilters=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&nextItemToken=0&resultSize=100&searchURL=&savedSearchId=&isAutoRefreshCall=false&notificationId=&auditContextMap={%22rlbChannel%22:%22EXACT_MATCH%22}"; 
		//&destinationCity=[object%20Object]
		//&originCity=[object%20Object]

  var statesArray=[];

  var startDate="";

  var startCityLatitude="";

  var startCityLongitude="";
  var startCityName="";
  var startCityStateCode="";
  var endCityName="";
  var endCityStateCode="";
  var endCityDisplayValue="", startCityDisplayValue="";
  		//&destinationCity=[object%20Object]
		//&originCity=[object%20Object]

  var minPricePerDistance="&minPricePerDistance=2";

  var startCityRadius="&startCityRadius=50";

  var endCityRadius="&endCityRadius=50";

  var endCityLatitude="";

  var endCityLongitude="";

  var minimumDurationInMillis="";

  var maximumDurationInMillis="";

  var minPayout="&minPayout=0";

  var maxPayout="&maxPayout=12000";

  var trailerStatusFilters="";

  var minDistance="";

  var maxDistance="";

  var startDate="";

  var endDate="";

  var stops=0;

  var workOpportunityType="";

  var loadingTypeFilters="";

  var driverTypeFilters="";

  var actualTime="";

  var bkt=1;

  var nyich=0;



    $("#origin").change(function(){  

    var this_el=this;

    var array = this_el.value.split(', ');

    var notfound=true;



    $.each(alloc, function( index, value ) {

        if(value.state==array[1] && value.city==array[0]){

          //this_el.attr("lat", value.lat).attr("lon", value.lon);

          startCityLatitude="&startCityLatitude="+value.lat;

          startCityLongitude="&startCityLongitude="+value.lon;
          startCityStateCode="&startCityStateCode="+array[1];
          startCityName="&startCityName="+array[0];
          startCityDisplayValue="&startCityDisplayValue="+array[0]+", "+array[1];

          console.log("origin: "+  startCityLatitude, startCityLongitude,startCityStateCode,startCityName);         

          notfound=false;

          return;

      }

  

    });

    if(notfound){

      startCityLatitude="";

      startCityLongitude="";

          startCityStateCode="";
          startCityName="";

     // this_el.removeAttr("lat").removeAttr("lon");

      alert("Could not find "+this.value+" try to write in a different way");

    }      

    });





    $("#r1").change(function(){

          //var url="https://relay.amazon.com/api/tours/loadboard/filters/cities/search/"+this.value; 

          //https://relay.amazon.com/api/tours/loadboard?sortByField=startTime&sortOrder=asc&nextItemToken=0&resultSize=100&searchURL=&savedSearchId=&notificationId=

      var r1 = this.value;



      if(r1>0)

        startCityRadius="&startCityRadius="+r1;

      else

        startCityRadius="";

      console.log("Org radius changed to "+r1);



    });





    $("#destination").change(function(){  

    var this_el=this;

    var array = this_el.value.split(', ');

    var notfound=true;



    $.each(alloc, function( index, value ) {

        if(value.state==array[1] && value.city==array[0]){

          //this_el.attr("lat", value.lat).attr("lon", value.lon);

          endCityLatitude="&endCityLatitude="+value.lat;

          endCityLongitude="&endCityLongitude="+value.lon;

          endCityStateCode="&endCityStateCode="+array[1];
          endCityName="&endCityName="+array[0];
          endCityDisplayValue="&startCityDisplayValue="+array[0]+", "+array[1]
          console.log("dst: "+ endCityLatitude, endCityLongitude,endCityName,endCityStateCode);         

          notfound=false;

          return;

      }

  

    });

    if(notfound){

      endCityLatitude="";

      endCityLongitude="";
      endCityStateCode="";
          endCityName="";

     // this_el.removeAttr("lat").removeAttr("lon");

      alert("Could not find "+this.value+" try to write in a different way");

    }      

    });





    $("#r2").change(function(){

          //var url="https://relay.amazon.com/api/tours/loadboard/filters/cities/search/"+this.value; 

          //https://relay.amazon.com/api/tours/loadboard?sortByField=startTime&sortOrder=asc&nextItemToken=0&resultSize=100&searchURL=&savedSearchId=&notificationId=

      var r2 = this.value;

      if(r2>0)

        endCityRadius="&endCityRadius="+r2;

      else

        endCityRadius="";

      console.log("Dst radius changed to "+r2);



    });



    $("#minpay").change(function(){

      var minpay = this.value;

      if(minpay>0)

        minPayout="&minPayout="+minpay;

      else

        minPayout="";

      console.log("minpay to "+minpay);



    });



    $("#maxpay").change(function(){

      var maxpay = this.value;

      if(maxpay>0)

        maxPayout="&minPayout="+maxpay;

      else

        maxPayout="";

      console.log("minpay to "+maxpay);



    });



    $("#mindis").change(function(){

      var mindis = this.value;

      if(mindis>0)

        minDistance="&minDistance="+mindis;

      else

        minDistance="";

      console.log("minDistance to "+mindis);



    });



    $("#maxdis").change(function(){

      var maxdis = this.value;

      if(maxdis>0)

        maxDistance="&maxDistance="+maxdis;

      else

        maxDistance="";

      console.log("maxDistance to "+maxdis);



    });



    $("#minhour").change(function(){

      var mindis = this.value;

      if(mindis>0)

        minimumDurationInMillis="&minimumDurationInMillis="+mindis*1000*60*60;

      else

        minimumDurationInMillis="";

      console.log("minimumDurationInMillis to "+mindis*1000*60*60);



    });



    $("#maxhour").change(function(){

      var maxdis = this.value;

      if(maxdis>0)

        maximumDurationInMillis="&maximumDurationInMillis="+maxdis*1000*60*60;

      else

        maximumDurationInMillis="";

      console.log("maximumDurationInMillis to "+maxdis*1000*60*60);



    });

//solo

     $("#solo").change(function(){

      var solo = this.value;

      if(solo!="NONE")

        

      driverTypeFilters="&driverTypeFilters="+solo;

      else

        driverTypeFilters="";

      console.log("driverTypeFilters to "+solo);



    });



    $("#trl").change(function(){

      var trl = this.value;

      if(trl!="NONE")

        trailerStatusFilters="&trailerStatusFilters="+trl;

      else

        trailerStatusFilters="";

      console.log("trailerStatusFilters to "+trl);



    });



    $("#trip_type").change(function(){

      var trip_type = this.value;

      if(trip_type=="ROUND_TRIP"){



          $("#dstcover").css('visibility', 'hidden');

        }

        else{

          $("#dstcover").css('visibility', 'visible');

        }     



      

      if(trip_type!="NONE")

        workOpportunityType="&workOpportunityType="+trip_type;

      else

        workOpportunityType="";

      console.log("workOpportunityType to "+trip_type);



    });



    $("#minper").change(function(){

      var minper = this.value;

      if(minper.length>0)

        minPricePerDistance="&minPricePerDistance="+minper;

      else

        minPricePerDistance="";

      console.log("minPricePerDistance to "+minper);



    });



    $("#time").change(function(){

      var time = this.value;

      if(time.length>0)

        startDate="&startDate="+time ;

      else

        startDate="";

      console.log("startDate to "+time);




    });



    $("#endtime").change(function(){

      var time = this.value;

      if(time.length>0)

        endDate="&endDate="+time;

      else

        endDate="";

      console.log("endDate to "+time);



    });



    $("#stops").change(function(){

      var st = this.value;

      if(st>0)

        stops=st;

      else

        stops=0;

      console.log("stops to "+st);



    }); 



    // $("#stops").change(function(){

    //   var st = this.value;

    //   if(st>0)

    //     stops=st;

    //   else

    //     stops=0;

    //   console.log("stops to "+st);



    // });



    $("#generate").click(function(){

       if( $("#nyichi").is(':checked')){

          nyich=1;

       }else{

          nyich=0;

       }

      

       $(".cts:checked").each(function () {

        var ar= new Array();

        //console.log($(this).attr('lat'));

        ar[0]=Number($(this).attr('lat'));

        ar[1]=Number($(this).attr('lon'));

        statesArray.push(ar);

       });



console.log(statesArray);

      urlBody="";

        if( $("#checkbox1").is(':checked')){

          console.log("empty trl yes");

            urlBody+="&startDate=" + $("#mpty").val() + "-04:00";

            actualTime=$("#time").val();

            /*var tmp=Number(actualTime.slice(11,13))+5;

            tmp=(tmp/10>=1)?tmp:"0"+tmp;

            actualTime=actualTime.slice(0,11)+tmp+actualTime.slice(13,19);*/



            var parsedDate = Date.parse(actualTime);

            parsedDate += 5*60*60*1000;

            var newDate = new Date(parsedDate);

            var dt=newDate ;

            var y=dt.getFullYear();

            var m=dt.getMonth()+1; m=(m/10>1)? m:"0"+m;

            var d=dt.getDate(); d=(d/10>=1)? d:"0"+d;



            var h=dt.getHours(); h=(h/10>=1)? h:"0"+h;

            var mn=dt.getMinutes(); mn=(mn/10>=1)? mn:"0"+mn;

            var s=dt.getSeconds(); s=(s/10>=1)? s:"0"+s;

            actualTime =y+"-"+m+"-"+d+"T"+h+":"+mn+":"+s+"Z";



            startDate="";

        }else{

            actualTime="";

            console.log("empty trl no");

        }



        if( workOpportunityType.length>0){

          if($("#trip_type").val()=="ROUND_TRIP"){

            endCityLatitude=""; endCityLongitude="";

            $("#destination").val("");

          }



            urlBody+=workOpportunityType;

        }else{

            console.log("no workOpportunityType");

        }





        if(startCityLatitude.length>0 && startCityLongitude.length>0){

            //console.log(startCityRadius);

            urlBody+=startCityLatitude+startCityLongitude+startCityRadius+startCityName+startCityStateCode+startCityDisplayValue+"&originCity=[object%20Object]";

            //console.log(urlBody);

        }else{

          console.log("no origin city data")

        }



        if(endCityLatitude.length>0 && endCityLongitude.length>0){

            //console.log(endCityRadius);

            urlBody+=endCityLatitude+endCityLongitude+endCityRadius+endCityName+endCityStateCode+endCityDisplayValue+"&destinationCity=[object%20Object]";

            

        }else{

          console.log("no dst city data")

        }

        if(minDistance.length>0){

            urlBody+=minDistance;

        }else{

            console.log("no mindis")

        }



        if( maxDistance.length>0){

            urlBody+=maxDistance;

        }else{

            console.log("no maxdis");

        }



        if(minPayout.length>0){

            urlBody+=minPayout;

        }else{

            console.log("no minPayout")

        }



        if( maxPayout.length>0){

            urlBody+=maxPayout;

        }else{

            console.log("no maxPayout");

        }



        if(minimumDurationInMillis.length>0){

            urlBody+=minimumDurationInMillis;

        }else{

            console.log("no minimumDurationInMillis")

        }



        if( maximumDurationInMillis.length>0){

            urlBody+=maximumDurationInMillis;

        }else{

            console.log("no maximumDurationInMillis");

        }



        if( minPricePerDistance.length>0){

            urlBody+=minPricePerDistance;

        }else{

            console.log("no minPricePerDistance");

        }



        if( trailerStatusFilters.length>0){

            urlBody+=trailerStatusFilters;

        }else{

            console.log("no trailerStatusFilters");

        }



        if( workOpportunityType.length>0){

            urlBody+=workOpportunityType;

        }else{

            console.log("no workOpportunityType");

        }



        if( startDate.length>0){

            urlBody+=startDate+"-04:00";

        }else{

            console.log("no startDate");

        }

        //driverTypeFilters

        if( driverTypeFilters.length>0){

            urlBody+=driverTypeFilters;

        }else{

            console.log("no driverTypeFilters");

        }

  if( endDate.length>0){

            urlBody+=endDate+"-04:00";

        }else{

            console.log("no endDate");

        }



       

        //alert(urlStart+urlBody+urlFoot);

        console.log(urlBody);

        $("#myInput").val("var url='"+urlStart+urlBody+urlFoot+"';var stops="+stops+";var actualTime='"+actualTime+"';var origincity='"+$("#origin").val()+" - "+$("#destination").val() +" ', payOut='"+$("#minpay").val()+"', perMile='"+$("#minper").val()+"',nyich="+nyich+"; var bkt="+$("#bk").val()+";var statesArray="+JSON.stringify(statesArray)+";clear();eval(localStorage.getItem('dsh_mnt'));");



        myFunction();

    });

    





    /*

      var url="";

  var urlStart="https://relay.amazon.com/api/tours/loadboard?sortByField=creationTime&sortOrder=desc";

  var urlBody="";

  var urlFoot="&equipmentTypeFilters=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&nextItemToken=0&resultSize=100&searchURL=&savedSearchId=&notificationId=";



  var startCityLatitude="";

  var startCityLongitude="";

  var startCityRadius="";

  var endCityRadius="&endCityRadius=50";

  var endCityLatitude="";


  var endCityLongitude="";

  var minimumDurationInMillis="";

  var maximumDurationInMillis="";

  var minPayout="&minPayout=0";

  var maxPayout="&maxPayout=12000";

  var minPricePerDistance="";

  var maxPricePerDistance="";

  var trailerStatusFilters="";


  var minDistance="";

  var maxDistance="";

  var startDate="";


  var workOpportunityType="";

  var loadingTypeFilters="";


    */
