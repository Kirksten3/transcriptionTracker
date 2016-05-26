$(document).ready(function(){

    var table = $("table.userInfo tbody");
    var names = [];
    var names2 = [];
    var titles = [];
    var titles2 = [];
    var experience = [];
    var expOG = [];
    var name = [];
    var eotw = [];
    var eotw2 = [];

    table.find('tr').each(function (i, el) {
        var $tds = $(this).find('td'),
            fName = $tds.eq(0).text(),
            lName = $tds.eq(1).text(),
            title = $tds.eq(4).text(),
            exp   = $tds.eq(3).text(),
            employee   = $tds.eq(5).text();

        name = fName + " " + lName;
        names.push(name);
        names2.push(name);
        titles.push(title);
        titles2.push(title);
        experience.push(exp);
        expOG.push(exp);
        eotw.push(employee);

    });

    experience.sort(function(a, b){return b-a;});

    for( var i = 0; i < name.length - 2; i++ )
    {
        names2[experience.indexOf(expOG[i])] = names[i];
        titles2[experience.indexOf(expOG[i])] = titles[i];
        eotw2[experience.indexOf(expOG[i])] = eotw[i];

    }


    var anna = (names2.indexOf("Anna Murphy")).toString();
    $("#pic" + anna).attr("src", "gui/assets/Anna.png");
    $("#level" + anna).text(titles2[anna]);
    if( eotw2[anna] == "Yes")
    {
        $("img#name" + anna ).attr("src", "gui/assets/Name Slot Gold.png");
        $("img#crown" + anna ).toggle();
    }

    var jacob = (names2.indexOf("Jacob Parpart")).toString();
    $("#pic" + jacob).attr("src", "gui/assets/Jacob.png");
    $("#level" + jacob).text(titles2[jacob]);
    if( eotw2[jacob] == "Yes")
    {
        $("img#name" + jacob).attr("src", "gui/assets/Name Slot Gold.png");
        $("img#crown" + jacob ).toggle();
    }

    var zach = (names2.indexOf("Zach Homen")).toString();
    $("#pic" + zach).attr("src", "gui/assets/Zach.png");
    $("#level" + zach).text(titles2[zach]);
    if( eotw2[zach] == "Yes")
    {
        $("img#name" + zach ).attr("src", "gui/assets/Name Slot Gold.png");
        $("img#crown" + zach ).toggle();
    }

    var kendall = (names2.indexOf("Kendall Henery")).toString();
    $("#pic" + kendall).attr("src", "gui/assets/Kendall.png");
    $("#level" + kendall).text(titles2[kendall]);
    if( eotw2[kendall] == "Yes")
    {
        $("img#name" + kendall ).attr("src", "gui/assets/Name Slot Gold.png");
        $("img#crown" + kendall ).toggle();
    }

    var madelyn = (names2.indexOf("Madelyn McQuilliam")).toString();
    $("#pic" + madelyn).attr("src", "gui/assets/Madelyn.png");
    $("#level" + madelyn).text(titles2[madelyn]);
    if( eotw2[madelyn] == "Yes")
    {
        $("img#name" + madelyn ).attr("src", "gui/assets/Name Slot Gold.png");
        $("img#crown" + madelyn ).toggle();
    }

    var graham = (names2.indexOf("Graham Founds")).toString();
    $("#pic" + graham).attr("src", "gui/assets/Graham.png");
    $("#level" + graham).text(titles2[graham]);
    if( eotw2[graham] == "Yes")
    {
        $("img#name" + graham ).attr("src", "gui/assets/Name Slot Gold.png");
        $("img#crown" + graham ).toggle();
    }



    var z = 0;

    $("#pic" + zach).click(
        function(){

        z = z + 1;

        if( z == 20 ){
            $("#pic0").attr("src", "gui/assets/Zach.png");
            $("#pic1").attr("src", "gui/assets/Zach.png");
            $("#pic2").attr("src", "gui/assets/Zach.png");
            $("#pic3").attr("src", "gui/assets/Zach.png");
            $("#pic4").attr("src", "gui/assets/Zach.png");
            $("#pic5").attr("src", "gui/assets/Zach.png");
        }});


//--------------------------ScoreBoard Name Hovers------------------------------------//


    $("img#pic0").mouseover(
        function () {
			if($("#crown0").is(":visible"))
			{
				$("#crown0").toggle();
				$("#crown0").toggleClass("hasCrown");
			}
            $("img#nameTip0").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#nameText0").text(names2[0]);
        });

    $("img#pic0").mouseout(
        function () {
			if($("#crown0").hasClass("hasCrown"))
			{
				$("#crown0").toggle();
				$("#crown0").toggleClass("hasCrown");
			}
            $("img#nameTip0").attr("src", "gui/assets/badges/tool tip empty.png");
			$("#nameText0").text("\xa0");
        });




    $("img#pic1").mouseover(
        function () {
			if($("#crown1").is(":visible"))
			{
				$("#crown1").toggle();
				$("#crown1").toggleClass("hasCrown");
			}
            $("img#nameTip1").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#nameText1").text(names2[1]);
        });

    $("img#pic1").mouseout(
        function () {
			if($("#crown1").hasClass("hasCrown"))
			{
				$("#crown1").toggle();
				$("#crown1").toggleClass("hasCrown");
			}
            $("img#nameTip1").attr("src", "gui/assets/badges/tool tip empty.png");
			$("#nameText1").text("\xa0");
        });
		
		
		
	$("img#pic2").mouseover(
        function () {
			if($("#crown2").is(":visible"))
			{
				$("#crown2").toggle();
				$("#crown2").toggleClass("hasCrown");
			}
            $("img#nameTip2").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#nameText2").text(names2[2]);
        });

    $("img#pic2").mouseout(
        function () {
			if($("#crown2").hasClass("hasCrown"))
			{
				$("#crown2").toggle();
				$("#crown2").toggleClass("hasCrown");
			}
			
            $("img#nameTip2").attr("src", "gui/assets/badges/tool tip empty.png");
			$("#nameText2").text("\xa0");
        });
		
		
		
		
	$("img#pic3").mouseover(
        function () {
			if($("#crown3").is(":visible"))
			{
				$("#crown3").toggle();
				$("#crown3").toggleClass("hasCrown");
			}
            $("img#nameTip3").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#nameText3").text(names2[3]);
        });

    $("img#pic3").mouseout(
        function () {
			if($("#crown3").hasClass("hasCrown"))
			{
				$("#crown3").toggle();
				$("#crown3").toggleClass("hasCrown");
			}			
            $("img#nameTip3").attr("src", "gui/assets/badges/tool tip empty.png");
			$("#nameText3").text("\xa0");
        });
		
		
		
		
	$("img#pic4").mouseover(
        function () {
			if($("#crown4").is(":visible"))
			{
				$("#crown4").toggle();
				$("#crown4").toggleClass("hasCrown");
			}			
            $("img#nameTip4").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#nameText4").text(names2[4]);
        });

    $("img#pic4").mouseout(
        function () {
			if($("#crown4").hasClass("hasCrown"))
			{
				$("#crown4").toggle();
				$("#crown4").toggleClass("hasCrown");
			}			
            $("img#nameTip4").attr("src", "gui/assets/badges/tool tip empty.png");
			$("#nameText4").text("\xa0");
        });
		
		
		
    $("img#pic5").mouseover(
        function () {
			if($("#crown5").is(":visible"))
			{
				$("#crown5").toggle();
				$("#crown5").toggleClass("hasCrown");
			}			
            $("img#nameTip5").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#nameText5").text(names2[5]);
        });

    $("img#pic5").mouseout(
        function () {
			if($("#crown5").hasClass("hasCrown"))
			{
				$("#crown5").toggle();
				$("#crown5").toggleClass("hasCrown");
			}			
            $("img#nameTip5").attr("src", "gui/assets/badges/tool tip empty.png");
			$("#nameText5").text("\xa0");
        });


});

$(document).ready(function(){
    var count = 0;
    var myBadges = [];
    var myBadge;


        $("ul.badges li").each(function() {
            $("img#mb" + count.toString() ).attr("src", "gui/assets/badges/" + this.innerHTML +".png");
            myBadges.push(this.innerHTML);
            count += 1;
        });

    for( var i = 0; i < 3; i++)
    {
        if( $("img#mb" + i.toString() ).attr("src") == "gui/assets/Placeholder.png")
        {
            $("img#mb" + i.toString() ).attr("src", "gui/assets/badges/empty.png");
            myBadges.push("Earn More Badges!");
        }
    }


    $("img#mb0").mouseover(
        function () {
            $("img.toolTip").attr("src", "gui/assets/badges/tool tip right.png");
            $(".toolText").text(myBadges[0]);
            $(".toolText").toggle();
        });

    $("img#mb0").mouseout(
        function () {
            $("img.toolTip").attr("src", "gui/assets/badges/tool tip empty.png");
            $(".toolText").toggle();
        });


    $("img#mb1").mouseover(
        function () {
            $("img.toolTip").attr("src", "gui/assets/badges/tool tip middle.png");
            $(".toolText").text(myBadges[1]);
            $(".toolText").toggle();
        });

    $("img#mb1").mouseout(
        function () {
            $("img.toolTip").attr("src", "gui/assets/badges/tool tip empty.png");
            $(".toolText").toggle();
        });


    $("img#mb2").mouseover(
        function () {
            $("img.toolTip").attr("src", "gui/assets/badges/tool tip left.png");
            $(".toolText").text(myBadges[2]);
            $(".toolText").toggle();
        });

    $("img#mb2").mouseout(
        function () {
            $("img.toolTip").attr("src", "gui/assets/badges/tool tip empty.png");
            $(".toolText").toggle();
        });





//---------------------------------------------------------------------------------------//



    $("img#p0b0").mouseover(
        function () {
            $("img#toolTip0").attr("src", "gui/assets/badges/sb-tool-tip-left.png");
            $("#toolText0").text("Placeholder Badge L");
        });

    $("img#p0b0").mouseout(
        function () {
            $("img#toolTip0").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText0").text("\xa0");
        });

    $("img#p0b1").mouseover(
        function () {
            $("img#toolTip0").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#toolText0").text("Placeholder Badge M");
        });

    $("img#p0b1").mouseout(
        function () {
            $("img#toolTip0").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText0").text("\xa0");
        });

    $("img#p0b2").mouseover(
        function () {
            $("img#toolTip0").attr("src", "gui/assets/badges/sb-tool-tip-right.png");
            $("#toolText0").text("Placeholder Badge R");
        });

    $("img#p0b2").mouseout(
        function () {
            $("img#toolTip0").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText0").text("\xa0");
        });


//---------------------------------------------------------------------------------------//



    $("img#p1b0").mouseover(
        function () {
            $("img#toolTip1").attr("src", "gui/assets/badges/sb-tool-tip-left.png");
            $("#toolText1").text("Placeholder Badge L");
        });

    $("img#p1b0").mouseout(
        function () {
            $("img#toolTip1").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText1").text("\xa0");
        });

    $("img#p1b1").mouseover(
        function () {
            $("img#toolTip1").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#toolText1").text("Placeholder Badge M");
        });

    $("img#p1b1").mouseout(
        function () {
            $("img#toolTip1").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText1").text("\xa0");
        });

    $("img#p1b2").mouseover(
        function () {
            $("img#toolTip1").attr("src", "gui/assets/badges/sb-tool-tip-right.png");
            $("#toolText1").text("Placeholder Badge R");
        });

    $("img#p1b2").mouseout(
        function () {
            $("img#toolTip1").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText1").text("\xa0");
        });


//---------------------------------------------------------------------------------------//




//---------------------------------------------------------------------------------------//



    $("img#p2b0").mouseover(
        function () {
            $("img#toolTip2").attr("src", "gui/assets/badges/sb-tool-tip-left.png");
            $("#toolText2").text("Placeholder Badge L");
        });

    $("img#p2b0").mouseout(
        function () {
            $("img#toolTip2").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText2").text("\xa0");
        });

    $("img#p2b1").mouseover(
        function () {
            $("img#toolTip2").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#toolText2").text("Placeholder Badge M");
        });

    $("img#p2b1").mouseout(
        function () {
            $("img#toolTip2").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText2").text("\xa0");
        });

    $("img#p2b2").mouseover(
        function () {
            $("img#toolTip2").attr("src", "gui/assets/badges/sb-tool-tip-right.png");
            $("#toolText2").text("Placeholder Badge R");
        });

    $("img#p2b2").mouseout(
        function () {
            $("img#toolTip2").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText2").text("\xa0");
        });


//---------------------------------------------------------------------------------------//



    $("img#p3b0").mouseover(
        function () {
            $("img#toolTip3").attr("src", "gui/assets/badges/sb-tool-tip-left.png");
            $("#toolText3").text("Placeholder Badge L");
        });

    $("img#p3b0").mouseout(
        function () {
            $("img#toolTip3").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText3").text("\xa0");
        });

    $("img#p3b1").mouseover(
        function () {
            $("img#toolTip3").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#toolText3").text("Placeholder Badge M");
        });

    $("img#p3b1").mouseout(
        function () {
            $("img#toolTip3").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText3").text("\xa0");
        });

    $("img#p3b2").mouseover(
        function () {
            $("img#toolTip3").attr("src", "gui/assets/badges/sb-tool-tip-right.png");
            $("#toolText3").text("Placeholder Badge R");
        });

    $("img#p3b2").mouseout(
        function () {
            $("img#toolTip3").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText3").text("\xa0");
        });


//---------------------------------------------------------------------------------------//



//---------------------------------------------------------------------------------------//



    $("img#p4b0").mouseover(
        function () {
            $("img#toolTip4").attr("src", "gui/assets/badges/sb-tool-tip-left.png");
            $("#toolText4").text("Placeholder Badge L");
        });

    $("img#p4b0").mouseout(
        function () {
            $("img#toolTip4").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText4").text("\xa0");
        });

    $("img#p4b1").mouseover(
        function () {
            $("img#toolTip4").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#toolText4").text("Placeholder Badge M");
        });

    $("img#p4b1").mouseout(
        function () {
            $("img#toolTip4").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText4").text("\xa0");
        });

    $("img#p4b2").mouseover(
        function () {
            $("img#toolTip4").attr("src", "gui/assets/badges/sb-tool-tip-right.png");
            $("#toolText4").text("Placeholder Badge R");
        });

    $("img#p4b2").mouseout(
        function () {
            $("img#toolTip4").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText4").text("\xa0");
        });


//---------------------------------------------------------------------------------------//



    $("img#p5b0").mouseover(
        function () {
            $("img#toolTip5").attr("src", "gui/assets/badges/sb-tool-tip-left.png");
            $("#toolText5").text("Placeholder Badge L");
        });

    $("img#p5b0").mouseout(
        function () {
            $("img#toolTip5").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText5").text("\xa0");
        });

    $("img#p5b1").mouseover(
        function () {
            $("img#toolTip5").attr("src", "gui/assets/badges/sb-tool-tip-middle.png");
            $("#toolText5").text("Placeholder Badge M");
        });

    $("img#p5b1").mouseout(
        function () {
            $("img#toolTip5").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText5").text("\xa0");
        });

    $("img#p5b2").mouseover(
        function () {
            $("img#toolTip5").attr("src", "gui/assets/badges/sb-tool-tip-right.png");
            $("#toolText5").text("Placeholder Badge R");
        });

    $("img#p5b2").mouseout(
        function () {
            $("img#toolTip5").attr("src", "gui/assets/badges/tool tip empty.png");
            $("#toolText5").text("\xa0");
        });


//---------------------------------------------------------------------------------------//




});

$(document).ready(function(){

    $("input.update").mouseover(
        function(){
            $("input.update").attr("src", "gui/assets/Check-2.png");
        });

    $("input.update").mouseout(
        function() {
            $("input.update").attr("src", "gui/assets/Check-1.png");
        });

});

$(document).ready(function(){

    $("img.scoreboardArrow").mouseover(
        function(){
            $("img.scoreboardArrow").attr("src", "gui/assets/RightArrow2.png");
        });

    $("img.scoreboardArrow").mouseout(
        function() {
            $("img.scoreboardArrow").attr("src", "gui/assets/RightArrow.png");
        });



    $("img.add").mouseover(
        function(){
            $("img.add").attr("src", "gui/assets/add2.png");

        }
    );

    var count = 0;


    $("img.add").click(function(){
    if(count == 0)
    {

        $("img.add").animate({  borderSpacing: +45 }, {
            step: function(now,fx) {
                $(this).css('-webkit-transform','rotate('+now+'deg)');
                $(this).css('-moz-transform','rotate('+now+'deg)');
                $(this).css('transform','rotate('+now+'deg)');
            },
            duration:''
        },'linear');

        $("div.newfoundContent").animate({ "left": "+=100em"});
        $("div.newfoundInput").animate({ "left": "-=94.7em"});

        setTimeout(function () {
        }, 400);

        count = 1;
    }

    else if(count == 1)
    {

        $("img.add").animate({  borderSpacing: 0 }, {
            step: function(now,fx) {
                $(this).css('-webkit-transform','rotate('+now+'deg)');
                $(this).css('-moz-transform','rotate('+now+'deg)');
                $(this).css('transform','rotate('+now+'deg)');
            },
            duration:''
        },'linear');

        $("div.newfoundContent").animate({ "left": "-=100em"});
        $("div.newfoundInput").animate({ "left": "+=94.7em"});

        setTimeout(function () {
        }, 400);

        count = 0;
    }
    });


    $("img.add").mouseout(
        function() {
            $("img.add").attr("src", "gui/assets/add1.png");
        });



    $("img.LA").mouseover(
        function(){
            $("img.LA").attr("src", "gui/assets/LA2.png");
        });

    $("img.LA").mouseout(
        function() {
            $("img.LA").attr("src", "gui/assets/LA1.png");
        });



    $("img.RA").mouseover(
        function(){
            $("img.RA").attr("src", "gui/assets/RA2.png");
        });

    $("img.RA").mouseout(
        function() {
            $("img.RA").attr("src", "gui/assets/RA1.png");
        });










    //---------------------Badge Expansion-----------------------//

    $(".myBadge").click(function () {

        $("div.hours").toggleClass("badgeClick");


        if($("div.hours").hasClass("badgeClick"))
        {
            $("div.hours").fadeToggle("slow");
            $("#myBadgeHolder1").fadeToggle("slow");
            $("#myBadgeHolder2").fadeToggle("slow");
        }
        else
        {
            $("#myBadgeHolder1").fadeToggle("slow");
            $("#myBadgeHolder2").fadeToggle("slow");
            $("div.hours").fadeToggle("slow");
        }

    });

});

$(document).ready(function(){

        $(".scoreboardArrow").click(function () {

            if($("div.rightContent").is(":visible")) {
                $("div.rightContent").fadeToggle("slow");
                $("div.newfoundInput").fadeToggle("slow");

                setTimeout(function () {
                    $("div.exp").fadeToggle("slow");
                }, 620);


            }
            else{
                $("div.exp").fadeToggle("slow");

                setTimeout(function () {
                    $("div.rightContent").fadeToggle("slow");
                    $("div.newfoundInput").fadeToggle("slow");
                }, 620);


            }


        });


    $(".RA").click(function () {

        $("div.newfoundText").fadeToggle("slow");
        $("img#newfoundPic").fadeToggle("slow");


        setTimeout(function () {
            $("div.newfoundText").text("Now the text is different and hopefully informative, and it will change the picture and text to a new person's fact");
        },800);

        setTimeout(function () {
            $("div.newfoundText").fadeToggle("slow");
            $("img#newfoundPic").fadeToggle("slow");
        },800);

    });


    $(".LA").click(function () {

        $("div.newfoundText").fadeToggle("slow");
        $("img#newfoundPic").fadeToggle("slow");

        setTimeout(function () {
            $("div.newfoundText").text("Now the text is different and hopefully informative, and it will change the picture and text to a new person's fact");
        },800);

        setTimeout(function () {
            $("div.newfoundText").fadeToggle("slow");
            $("img#newfoundPic").fadeToggle("slow");
        },800);

    });

});



$(document).ready(function(){

    var fName = $("p.firstName").text();
    var lName = $("p.lastName").text();

    var name = fName + " " + lName;

	console.log(fName);
	fName = fName.trim();

    $("#myPic").attr("src","gui/assets/" + fName + ".png");
    $("#myPic2").attr("src", "gui/assets/" + fName + ".png");

});


$(document).ready(function(){

    var expBar = $("p.myExp").text();
    var expRound;

    $("div#expNumber0").text(expBar);
    if(expBar >= 0 && expBar < 1500 )
    {
        $('div#expNumber0').css({ 'left': '24.4em' });
        $("div#expNumber2").text("1500");
    }
    else if(expBar >= 1500 && expBar < 3000)
    {
        $("div#expNumber2").text("3000");
    }
    else if(expBar >= 3000 && expBar < 5000)
    {
        $("div#expNumber2").text("5000");
    }
    else if(expBar >= 5000 && expBar < 7500)
    {
        $("div#expNumber2").text("7500");
    }
    else if(expBar >= 7500)
    {
        $("div#expNumber2").text("");
        $("div#expNumber1").text("");
        $('div#expNumber0').css({ 'left': '25.1em' });

    }


    if(expBar >= 0 && expBar < 1500 )
    {
        $("div.currLevel").text("Novice");
        $("div.nextLevel").text("Apprentice");

        expRound = 50 * Math.round(expBar/50);

        $("img.expBar").attr("src", "gui/assets/progress bar/" + expRound.toString() + ".png");
    }
    else if(expBar >= 1500 && expBar < 3000)
    {
        $("div.currLevel").text("Apprentice");
        $("div.nextLevel").text("Journeyman");
        $('div.nextLevel').css({ 'left': '19.5em' });

        expBar = expBar - 1500;
        expRound = 50 * Math.round(expBar/50);

        $("img.expBar").attr("src", "gui/assets/progress bar/" + expRound.toString() + ".png");
    }
    else if(expBar >= 3000 && expBar < 5000)
    {
        $("div.currLevel").text("Journeyman");
        $("div.nextLevel").text("Expert");
        $('div.nextLevel').css({ 'left': '22em' });

        expBar = expBar - 3000;

        if( expBar > 200 && expBar < 400)       {expBar = expBar - 50; }
        if( expBar >= 400 && expBar < 600)      {expBar = expBar - 150;}
        if( expBar >= 600 && expBar < 1000)     {expBar = expBar - 250;}
        if( expBar >= 1000 && expBar < 1250)    {expBar = expBar - 300;}
        if( expBar >= 1250 && expBar < 1500)    {expBar = expBar - 350;}
        if( expBar >= 1500 && expBar < 1750)    {expBar = expBar - 450;}
        if( expBar >= 1750 && expBar < 2000)    {expBar = expBar - 500;}
        expRound = 50 * Math.round(expBar/50);

        $("img.expBar").attr("src", "gui/assets/progress bar/" + expRound.toString() + ".png");
    }
    else if(expBar >= 5000 && expBar < 7500)
    {
        $("div.currLevel").text("Expert");
        $("div.nextLevel").text("Master");
        $('div.nextLevel').css({ 'left': '22em' });

        expBar = expBar - 5000;

        if( expBar > 200 && expBar < 400)       {expBar = expBar - 50; }
        if( expBar >= 400 && expBar < 600)      {expBar = expBar - 150;}
        if( expBar >= 600 && expBar < 1000)     {expBar = expBar - 200;}
        if( expBar >= 1000 && expBar < 1250)    {expBar = expBar - 250;}
        if( expBar >= 1250 && expBar < 1500)    {expBar = expBar - 350;}
        if( expBar >= 1500 && expBar < 1750)    {expBar = expBar - 550;}
        if( expBar >= 1750 && expBar < 2000)    {expBar = expBar - 750;}
        if( expBar >= 2000 && expBar < 2250)    {expBar = expBar - 850;}
        if( expBar >= 2250 && expBar < 2400)    {expBar = expBar - 950;}
        if( expBar >= 2400 && expBar < 2500)    {expBar = expBar - 1000;}
        expRound = 50 * Math.round(expBar/50);

        $("img.expBar").attr("src", "gui/assets/progress bar/" + expRound.toString() + ".png");
    }
    else if(expBar >= 7500)
    {
        $("div.currLevel").text("Master");
        $("div.nextLevel").text("");
        $("img.expBar").attr("src", "gui/assets/progress bar/1500.png");
        $('div.hours').css({ 'top': '-8.2em' });
    }


    $("img.expBar").mouseover(
        function(){
            $("div.expNumber").fadeToggle("fast");
        });

    $("img.expBar").mouseout(
        function() {
            $("div.expNumber").fadeToggle("fast");
        });

    $("div.submit").click(function () {

        if( $("textarea.newfoundFact").val() == "Kevin Ahern")
        {
            $('body').css('background-image','url(test.png)');
            $(".animationBlock").fadeToggle("fast");

            $("#pic0").attr("src", "gui/assets/test.png");
            $("#pic1").attr("src", "gui/assets/test.png");
            $("#pic2").attr("src", "gui/assets/test.png");
            $("#pic3").attr("src", "gui/assets/test.png");
            $("#pic4").attr("src", "gui/assets/test.png");
            $("#pic5").attr("src", "gui/assets/test.png");
            $("#myPic").attr("src", "gui/assets/test.png");
            $("#myPic2").attr("src", "gui/assets/test.png");
            $(".badge").attr("src", "gui/assets/test.png");
            $(".myBadge").attr("src", "gui/assets/test.png");
            $("#newfoundPic").attr("src", "gui/assets/test.png");
        }
    });

    });

