console.log("loaded");


    $('input[id^="origin"]').change(function(){  
//alert(111);
    var this_el=this;
    if(this_el.value.length==0) {
        $(this_el).removeAttr("loc");
        $(this_el).removeAttr("lon");
         $(this_el).removeAttr("lat");
         $(this_el).removeAttr("citiName");
         return;
    }
    var array = this_el.value.split(', ');

    var notfound=true;



    $.each(alloc, function( index, value ) {

        if(value.state==array[1] && value.city==array[0]){

          //this_el.attr("lat", value.lat).attr("lon", value.lon);

          $(this_el).attr("loc", [value.lat, value.lon]);
          $(this_el).attr("lon", value.lon);
          $(this_el).attr("lat", value.lat);
          $(this_el).attr("citiName", value.city+", "+value.state);

          //console.log("origin for "+$(this_el).attr('id')+" : "+  array[0], array[1],value.lon,value.lat);         

          notfound=false;

          return;

      }

  

    });

    if(notfound){

     // this_el.removeAttr("lat").removeAttr("lon");
      $(this_el).removeAttr("loc");
        $(this_el).removeAttr("lon");
         $(this_el).removeAttr("lat");
         $(this_el).removeAttr("citiName");
        
        this_el.value='';
      alert("Could not find "+this.value+" try to write in a different way");

    }      

    });
    $('input[id^="destination"]').change(function(){  
//alert(111);
    var this_el=this;
    if(this_el.value.length==0) {
        $(this_el).removeAttr("loc");
        $(this_el).removeAttr("lon");
         $(this_el).removeAttr("lat");
         $(this_el).removeAttr("citiName");

         return;
    }
    var array = this_el.value.split(', ');

    var notfound=true;



    $.each(alloc, function( index, value ) {

        if(value.state==array[1] && value.city==array[0]){

          //this_el.attr("lat", value.lat).attr("lon", value.lon);

          $(this_el).attr("loc", [value.lat, value.lon]);
          $(this_el).attr("lon", value.lon);
          $(this_el).attr("lat", value.lat);
          $(this_el).attr("citiName", value.city+", "+value.state);

          //console.log("destination for "+$(this_el).attr('id')+" : "+  array[0], array[1],value.lon,value.lat);         

          notfound=false;

          return;

      }

  

    });

    if(notfound){

     // this_el.removeAttr("lat").removeAttr("lon");
      $(this_el).removeAttr("loc");
        $(this_el).removeAttr("lon");
         $(this_el).removeAttr("lat");
         $(this_el).removeAttr("citiName");
        
         this_el.value='';
      alert("Could not find "+this.value+" try to write in a different way");

    }      

    });

    $('input[id^="time"]').change(function(){  
//alert(111);
    var this_el=this;

    var parsedDate = Date.parse(this_el.value);
    if(!parsedDate) {
      alert("Wrong date format");
      this_el.value='';
    }
    });

    $('input[id^="endtime"]').change(function(){  
//alert(111);
    var this_el=this;

    var parsedDate = Date.parse(this_el.value);
    if(!parsedDate) {
      alert("Wrong date format");
      this_el.value='';
    }
    });
 $("#copy").click(function(){
        var statesArray=[];
        // var tmpB="https://relay.amazon.com/api/tours/loadboard?sortByField=creationTime&sortOrder=desc&minPayout="+$("#gminpay").val()+"&maxPayout=12000&minPricePerDistance="+$("#gminper").val()+"&maxPricePerDistance=30&equipmentTypeFilters=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&equipmentTypes=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&nextItemToken=0&resultSize=100&searchURL=&savedSearchId=&isAutoRefreshCall=false&notificationId="
        //prosto rate per mile        
        var url="https://relay.amazon.com/api/tours/loadboard?sortByField=creationTime&sortOrder=desc&minPayout="+$("#gminpay").val()+"&maxPayout=12000&minPricePerDistance="+$("#gminper").val()+"&maxPricePerDistance=30&trailerStatusFilters=PROVIDED&trailerStatus=PROVIDED&equipmentTypeFilters=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&equipmentTypes=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&nextItemToken=0&resultSize=100&searchURL=&savedSearchId=&isAutoRefreshCall=false&notificationId=&auditContextMap={%22rlbChannel%22:%22EXACT_MATCH%22,%22isOriginCityLive%22:%22false%22,%22isDestinationCityLive%22:%22false%22}"
        //san bernardino 1500
        // var url="https://relay.amazon.com/api/tours/loadboard?sortByField=creationTime&sortOrder=desc&endCityLatitude=34.841435&endCityLongitude=-116.178456&endCityRadius=1500&endCityName=SAN%20BERNARDINO&endCityStateCode=CA&endCityDisplayValue=SAN%20BERNARDINO,%20CA&isDestinationCityLive=false&destinationCity=[object%20Object]&minPayout="+$("#gminpay").val()+"&maxPayout=12000&minPricePerDistance="+$("#gminper").val()+"&maxPricePerDistance=30&trailerStatusFilters=PROVIDED&trailerStatus=PROVIDED&equipmentTypeFilters=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&equipmentTypes=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&nextItemToken=0&resultSize=100&searchURL=&savedSearchId=&isAutoRefreshCall=false&notificationId=&auditContextMap={%22rlbChannel%22:%22EXACT_MATCH%22,%22isOriginCityLive%22:%22false%22,%22isDestinationCityLive%22:%22false%22}"
        $(".cts:checked").each(function () {
        var ar= new Array();
        //console.log($(this).attr('lat'));
        ar[0]=Number($(this).attr('lat'));
        ar[1]=Number($(this).attr('lon'));
        statesArray.push(ar);
       });
        bigJSON = bigJSON.filter(function(el) {    return (el != null && el!=0);});
        //console.log(bigJSON);
        
        var STRINGTOPRINT = " "
        var sts=""
        bigJSON.forEach(function(item, index){
            STRINGTOPRINT+=item["puName"]+" | ";
            sts+=(item["puName"]).slice(-2)+"-";
        })
        STRINGTOPRINT += " "
        console.clear();
        console.log("bigJSON="+JSON.stringify(bigJSON, null,2)+"\n\nSTRINGTOPRINT="+STRINGTOPRINT+"\n\nurl='"+url+"'")
        $("#myInput").val('STRINGTOPRINT="'+STRINGTOPRINT+'"\n\nurl="'+url+'"\n\nbigJSON='+JSON.stringify(bigJSON, null,2)) //+"\n statesArray="+JSON.stringify(statesArray,null,2)+",                                                                          tmpB ='"+tmpB+"';clear();bigJSON = bigJSON.filter(function(el) {    return (el != null && el!=0);}); eval(localStorage.getItem('csm-bfhsb'));");
        statesArray=0;
        // prepBigJson=JSON.stringify(bigJSON)
        // readyBigJson=prepBigJson.replace(/["]/g, "'")
        myFunction();
        download(sts+".cmd",'echo Starting\n\npython C:/Users/Administrator/one1/mastermany.py "'+url+'" "'+STRINGTOPRINT+'" "'+JSON.stringify(bigJSON)+'"\n\necho Finished\npause')

    });

function myFunction() {
  var copyText = document.getElementById("myInput");
  copyText.select();
  copyText.setSelectionRange(0, 99999)
  document.execCommand("copy");
  // alert("Copied the text: " );
}

function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

   $('form[id^="f__"]').children().change(function(){  
//alert(111);
    $(this).parent().css("background-color","white"); 
    
    });

