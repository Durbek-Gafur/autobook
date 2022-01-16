var LoadObject = function(puLon, puLat, puTime, delLon, delLat, delTime, trlStat, tripType, isTeam, stopsCount, nyIchi, puName, delName, payOut, perMile, minDis, maxDis, puRad, delRad, book,pickLabels,delLabels){
    
    // this.puTime=puTime;

    // this.delTime=delTime;
    // this.trlStat=trlStat;       //0 - po 1 - req 2 - any
    // this.tripType=tripType;     //0 - rt 1 - one way 2 - any
    // this.isTeam=isTeam;         //0 - solo 1 - team 2 - any
    // this.stopsCount=stopsCount;
    // this.nyIchi=nyIchi;


    // this.minDis=minDis;
    // this.maxDis=maxDis;
    this.puName=puName;
    this.puRad=puRad;
    this.puLon=puLon;
    this.puLat=puLat;


    this.delName=delName;
    this.delRad=delRad;
    this.delLon=delLon;
    this.delLat=delLat;

    this.payOut=payOut;
    this.perMile=perMile;
    // this.pickLabels=pickLabels;
    // this.delLabels=delLabels;
    // this.book=book;
}
var bigJSON=new Array()
//for(i=0;i<10;i++) bigJSON[i]=0;
LoadObject.prototype.stringify = function() {
    console.log(JSON.stringify(this))
      // console.log("book: "+this.book+"\npuName "+this.puName+"\npuRad "+this.puRad+"\ndelName "+this.delName+"\ndelRad "+this.delRad+"\npayOut "+this.payOut +"\nperMile "+this.perMile +"\nminDis "+this.minDis +"\nmaxDis "+this.maxDis+"\npuLon "+this.puLon+"\npuLat "+this.puLat+"\npuTime "+this.puTime+"\ndelLon "+this.delLon+"\ndelLat "+this.delLat+"\ndelTime "+this.delTime+"\ntrlStat "+this.trlStat +"\ntripType "+this.tripType+"\nisTeam "+this.isTeam +"\nstopsCount "+this.stopsCount+"\nnyIchi "+this.nyIchi);
  
};



 function strr(thisL) {
  
    console.log(JSON.stringify(thisL))
    // console.log("book: "+thisL.book+"\npuName "+thisL.puName+"\npuRad "+thisL.puRad+"\ndelName "+thisL.delName+"\ndelRad "+thisL.delRad+"\npayOut "+thisL.payOut +"\nperMile "+thisL.perMile +"\nminDis "+thisL.minDis +"\nmaxDis "+thisL.maxDis+"\npuLon "+thisL.puLon+"\npuLat "+thisL.puLat+"\npuTime "+thisL.puTime+"\ndelLon "+thisL.delLon+"\ndelLat "+thisL.delLat+"\ndelTime "+thisL.delTime+"\ntrlStat "+thisL.trlStat +"\ntripType "+thisL.tripType+"\nisTeam "+thisL.isTeam +"\nstopsCount "+thisL.stopsCount+"\nnyIchi "+thisL.nyIchi);
  
}


function getAllLoads(){
    loads.forEach(function(e, i){console.log("Load ["+i+"]"); e.stringify()});    
}

function distance(lat1, lon1, lat2, lon2) {
    if ((lat1 == lat2) && (lon1 == lon2)) {
        return 0;
    } else {
        var radlat1 = Math.PI * lat1 / 180;
        var radlat2 = Math.PI * lat2 / 180;
        var theta = lon1 - lon2;
        var radtheta = Math.PI * theta / 180;
        var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
        if (dist > 1) {
            dist = 1;
        }
        dist = Math.acos(dist);
        dist = dist * 180 / Math.PI;
        dist = dist * 60 * 1.1515;

        return dist;
    }
}


function getLabels(lat, lon, rad){

    labels=[]
    if(lat==0 || lon==0)
        return false
    $.each(mylocs, function(index, loc) {
        if(rad>distance(lat, lon, Number(loc.latitude), Number(loc.longitude)))
            if(!(labels.includes(loc.label)))
            labels.push(loc.label);
    })
    return labels;

}
$('button[id^="generate"]').click(function(){
    var id=$(this).attr("id");
    var index=id.slice(10);
    var puLon = Number( ($("#origin__"+index).attr('lon'))?$("#origin__"+index).attr('lon'):0 );
    var puLat = Number(($("#origin__"+index).attr('lat'))?$("#origin__"+index).attr('lat'):0);
    var puTime = getTime("#time__"+index);
    var delLon =Number( ($("#destination__"+index).attr('lon'))?$("#destination__"+index).attr('lon'):0);
    var delLat = Number(($("#destination__"+index).attr('lat'))?$("#destination__"+index).attr('lat'):0);
    var delTime = getTime("#endtime__"+index);
    var trlStat = $("#trl__"+index).val();       //0 - po 1 - req 2 - any
    var tripType = $("#trip_type__"+index).val();     //0 - rt 1 - one way 2 - any
    var isTeam = $("#solo__"+index).val();         //0 - solo 1 - team 2 - any
    var payOut = Number($("#minpay__"+index).val()); 
    var perMile = Number($("#minper__"+index).val()); 
    var minDis =Number( $("#mindis__"+index).val()); 
    var maxDis =Number( $("#maxdis__"+index).val()); 
    var puRad = Number($("#r1__"+index).val()); 
    var delRad = Number($("#r2__"+index).val()); 
    var stopsCount = Number($("#stops__"+index).val());
    var nyIchi = ( $("#nyichi__"+index).is(':checked'))? 1 : 0;
    var puName = ($("#origin__"+index).attr('citiname'))?$("#origin__"+index).attr('citiname'):0;
    var delName = ($("#destination__"+index).attr('citiname'))?$("#destination__"+index).attr('citiname'):0;
    var book = Number($("#bk__"+index).val());

    var pickLabels=getLabels(puLat, puLon, puRad)
    var delLabels=getLabels(delLat, delLon, delRad)
    var loadInstance = new LoadObject(puLon, puLat, puTime, delLon, delLat, delTime, trlStat, tripType, isTeam, stopsCount, nyIchi, puName, delName, payOut, perMile, minDis, maxDis,puRad,delRad,book,pickLabels,delLabels);
    bigJSON[index] = loadInstance;
    //console.log(pickLabels);
    //console.log(delLabels);
    loadInstance.stringify();
    $("#f__"+index).css("background-color","aliceblue"); 
    
});

$('button[id^="remove"]').click(function(){
    var id=$(this).attr("id");
    var index=id.slice(8);
    $("#origin__"+index).removeAttr('lon');
    $("#origin__"+index).removeAttr('lat');
    $("#time__"+index).val("");
    $("#destination__"+index).removeAttr('lon');
    $("#destination__"+index).removeAttr('lat');
    $("#endtime__"+index).val("");
    $("#trl__"+index).val($("#trl__"+index+" option:first").val());
    $("#trip_type__"+index).val($("#trip_type__"+index+" option:first").val());
    $("#solo__"+index).val($("#solo__"+index+" option:first").val());
    $("#minpay__"+index).val(0);
    $("#minper__"+index).val(2); 
    $("#mindis__"+index).val(10); 
    $("#maxdis__"+index).val(9999); 
    $("#stops__"+index).val(1);;
    $("#nyichi__"+index).prop("checked", false);
    $("#origin__"+index).removeAttr('citiname');
    $("#origin__"+index).val("");
    $("#destination__"+index).removeAttr('citiname');
    $("#destination__"+index).val("");
    $("#r1__"+index).val(50); 
    $("#r2__"+index).val(50); 
    $("bk__"+index).val(1);  
    console.log("Removing: "+bigJSON[index].puName+"-"+bigJSON[index].delName)  
    bigJSON.splice(index,1);
    //bigJSON[index]=0;
    $("#f__"+index).css("background-color","white"); 
    
});


function getTime(id){
    var actualTime=$(id).val();
    if(!actualTime) return 0;
    var parsedDate = Date.parse(actualTime);
    if(!parsedDate) return 0;
        parsedDate += 4*60*60*1000;
    var newDate = new Date(parsedDate);
    var dt=newDate ;
    var y=dt.getFullYear();
    var m=dt.getMonth()+1; m=(m/10>1)? m:"0"+m;
    var d=dt.getDate(); d=(d/10>=1)? d:"0"+d;
    var h=dt.getHours(); h=(h/10>=1)? h:"0"+h;
    var mn=dt.getMinutes(); mn=(mn/10>=1)? mn:"0"+mn;
    var s=dt.getSeconds(); s=(s/10>=1)? s:"0"+s;
    actualTime =y+"-"+m+"-"+d+"T"+h+":"+mn+":"+s+"Z";
    return actualTime;
}
//
//var load2 = new LoadObject(2000, 1000, "11:30", 1111, 23432, "12:30", 2, 2, 2, 3, 1);
//var load3 = new LoadObject(2000, 1000, "11:30", 1111, 23432, "12:30", 2, 2, 2, 3, 1);
//loads.push(load1);loads.push(load2);loads.push(load3)