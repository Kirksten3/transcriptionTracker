<!DOCTYPE html>
<html><head>
  <title>Transcribe</title>

  <link rel="stylesheet" type="text/css" href="gui/stylesheet.css">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
  <script src="gui/scriptSource.js" type="text/javascript"></script>

</head>
<body>

<div id="wrapper">
<p id="notice"></p>


<h1 id="pageTitle">Transcription Tracker <div class = "tag">Pretend You're Having Fun</div></h1>

<div class="page">

<img src="gui/assets/Scoreboard.png" class = "scoreboard">
<div class = "titlefont"><div class = "scoretitle"> Scoreboard </div> </div>
<img src="gui/assets/RightArrow.png" class = "scoreboardArrow">

<div class = "users">

  <img src="gui/assets/Name Slot.png" class = "slots" id = "name0">
    <img src="gui/assets/Placeholder.png" class = "placeholder" id = "pic0">
    <div class = "level" id = "level0"> Level </div>
    <img src="gui/assets/badgeSlots.png" class = "badgeSlots" id = "badge0">
      <img src="gui/assets/badges/HORT/Ten Hours HORT.png" class = "badge" id = "p0b0">
      <img src="gui/assets/badges/HORT/Twenty Hours HORT.png" class = "badge" id = "p0b1">
      <img src="gui/assets/badges/HORT/Thirty Five Hours HORT.png" class = "badge" id = "p0b2">
        <img src="gui/assets/badges/tool tip empty.png" class = "SBToolTip" id = "toolTip0" />
        <div class = "SBToolText" id = "toolText0">&nbsp</div>
   	<img src="gui/assets/badges/tool tip empty.png" class = "nameTip" id = "nameTip0" />
        <div class = "nameText" id = "nameText0">&nbsp</div>
            <img src="gui/assets/Crown.png" class = "crown" id = "crown0">

  <img src="gui/assets/Name Slot.png" class = "slots" id = "name1">
    <img src="gui/assets/Placeholder.png" class = "placeholder" id = "pic1">
    <div class = "level" id = "level1"> Level </div>
    <img src="gui/assets/badgeSlots.png" class = "badgeSlots" id = "badge1">
      <img src="gui/assets/badges/FES/Ten Hours FES.png" class = "badge" id = "p1b0">
      <img src="gui/assets/badges/FES/Twenty Hours FES.png" class = "badge" id = "p1b1">
      <img src="gui/assets/badges/FES/Thirty Five Hours FES.png" class = "badge" id = "p1b2">
        <img src="gui/assets/badges/tool tip empty.png" class = "SBToolTip" id = "toolTip1" />
        <div class = "SBToolText" id = toolText1>&nbsp</div>
    <img src="gui/assets/badges/tool tip empty.png" class = "nameTip" id = "nameTip1" />
        <div class = "nameText" id = "nameText1">&nbsp</div>
            <img src="gui/assets/Crown.png" class = "crown" id = "crown1">

  <img src="gui/assets/Name Slot.png" class = "slots" id = "name2">
    <img src="gui/assets/Placeholder.png" class = "placeholder" id = "pic2">
    <div class = "level" id = "level2"> Level </div>
    <img src="gui/assets/badgeSlots.png" class = "badgeSlots" id = "badge2">
      <img src="gui/assets/badges/MTH/Ten Hours MTH.png" class = "badge" id = "p2b0">
      <img src="gui/assets/badges/MTH/Twenty Hours MTH.png" class = "badge" id = "p2b1">
      <img src="gui/assets/badges/MTH/Thirty Five Hours MTH.png" class = "badge" id = "p2b2">
        <img src="gui/assets/badges/tool tip empty.png" class = "SBToolTip" id = "toolTip2" />
        <div class = "SBToolText" id = toolText2>&nbsp</div>
    <img src="gui/assets/badges/tool tip empty.png" class = "nameTip" id = "nameTip2" />
        <div class = "nameText" id = "nameText2">&nbsp</div>
        	<img src="gui/assets/Crown.png" class = "crown" id = "crown2">

  <img src="gui/assets/Name Slot.png" class = "slots" id = "name3">
    <img src="gui/assets/Placeholder.png" class = "placeholder" id = "pic3">
    <div class = "level" id = "level3"> Level </div>
    <img src="gui/assets/badgeSlots.png" class = "badgeSlots" id = "badge3">
      <img src="gui/assets/badges/H/Ten Hours H.png" class = "badge" id = "p3b0">
      <img src="gui/assets/badges/H/Twenty Hours H.png" class = "badge" id = "p3b1">
      <img src="gui/assets/badges/H/Thirty Five Hours H.png" class = "badge" id = "p3b2">
        <img src="gui/assets/badges/tool tip empty.png" class = "SBToolTip" id = "toolTip3" />
        <div class = "SBToolText" id = toolText3>&nbsp</div>
    <img src="gui/assets/badges/tool tip empty.png" class = "nameTip" id = "nameTip3" />
        <div class = "nameText" id = "nameText3">&nbsp</div>
            <img src="gui/assets/Crown.png" class = "crown" id = "crown3">

  <img src="gui/assets/Name Slot.png" class = "slots" id = "name4">
    <img src="gui/assets/Placeholder.png" class = "placeholder" id = "pic4">
    <div class = "level" id = "level4"> Level </div>
    <img src="gui/assets/badgeSlots.png" class = "badgeSlots" id = "badge4">
      <img src="gui/assets/badges/BI/Ten Hours BI.png" class = "badge" id = "p4b0">
      <img src="gui/assets/badges/BI/Twenty Hours BI.png" class = "badge" id = "p4b1">
      <img src="gui/assets/badges/BI/Thirty Five Hours BI.png" class = "badge" id = "p4b2">
        <img src="gui/assets/badges/tool tip empty.png" class = "SBToolTip" id = "toolTip4" />
        <div class = "SBToolText" id = toolText4>&nbsp</div>
    <img src="gui/assets/badges/tool tip empty.png" class = "nameTip" id = "nameTip4" />
        <div class = "nameText" id = "nameText4">&nbsp</div>
            <img src="gui/assets/Crown.png" class = "crown" id = "crown4">

  <img src="gui/assets/Name Slot.png" class = "slots" id = "name5">
    <img src="gui/assets/Placeholder.png" class = "placeholder" id = "pic5">
    <div class = "level" id = "level5"> Level </div>
    <img src="gui/assets/badgeSlots.png" class = "badgeSlots" id = "badge5">
      <img src="gui/assets/badges/ANS/Ten Hours ANS.png" class = "badge" id = "p5b0">
      <img src="gui/assets/badges/ANS/Twenty Hours ANS.png" class = "badge" id = "p5b1">
      <img src="gui/assets/badges/ANS/Thirty Five Hours ANS.png" class = "badge" id = "p5b2">
        <img src="gui/assets/badges/tool tip empty.png" class = "SBToolTip" id = "toolTip5" />
        <div class = "SBToolText" id = toolText5>&nbsp</div>
    <img src="gui/assets/badges/tool tip empty.png" class = "nameTip" id = "nameTip5" />
        <div class = "nameText" id = "nameText5">&nbsp</div>
            <img src="gui/assets/Crown.png" class = "crown" id = "crown5">

</div>

  <img src="gui/assets/divider.png" class = "divider">

<div class = "rightContent">

<div class = "entryHolder">

<img src="gui/assets/New Entry.png" class = "entry">
<div class = "titlefont"><div class = "entrytitle"> New Entry </div> </div>



<form class="new_update" id="new_update" action="/users/13/updates" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="8UD2VPIPDmEE8pHcLu+ZmcrHkl9zR/XZpJ4PRUNqT+CwJeJVTbOM/MCOXg9UyeadTioTMuh8ukx38gL2E5NRMA==">

    <div class="field">
      <input type="text" name="update[lecture_length]" id="update_lecture_length" placeholder = "Length" class = "length">
    </div>
    <div class="field">
      <!--<input type="text" name="update[course_subject]" id="update_course_subject" />-->



      <select name="update[course_subject]" id="update_course_subject" class = "subject">
        <option value="" disabled selected>Subject</option>
        <option value="HORT">HORT</option>
        <option value="FES">FES</option>
        <option value="MTH">MTH</option>
        <option value="ANTH">ANTH</option>
        <option value="ANS">ANS</option>
        <option value="BI">BI</option>
        <option value="H">H</option></select>

    </div>
    <div class="actions">
      <input class = "update" type = "image" name="commit" src="gui/assets/Check-1.png">
    </div>

  </form>

</div>

<div class = "progressHolder">

<img src="gui/assets/Progress.png" class = "progress">
<div class = "titlefont"><div class = "progresstitle"> Progress </div> </div>
<img src="gui/assets/ProgressCircle.png" class = "progressCircle" class = "name3">
<img src="gui/assets/Placeholder.png" class = "placeholder" id = "myPic">
<img src="gui/assets/progress bar/0.png" class = "expBar">

  <img src="gui/assets/Placeholder.png" class = "myBadge" id = "mb2">
  <img src="gui/assets/Placeholder.png" class = "myBadge" id = "mb1">
  <img src="gui/assets/Placeholder.png" class = "myBadge" id = "mb0">

<div class="currLevel">Level</div>
<div class="nextLevel">Level</div>
<div class="expNumber" id = "expNumber0"> exp</div>
<div class="expNumber" id = "expNumber1">|</div>
<div class="expNumber" id = "expNumber2"> exp</div>

<div class = "hours">23 Hours Transcribed</div>


<img src="gui/assets/badgeSlots.png" class = "myBadgeHolder">
<img src="gui/assets/badgeSlots.png" class = "myBadgeHolder" id = "myBadgeHolder1">
<img src="gui/assets/badgeSlots.png" class = "myBadgeHolder" id = "myBadgeHolder2">

<img src="gui/assets/badges/tool tip empty.png" class = "toolTip"/>
<div class = "toolText">Placeholder Badge</div>

</div>

<div class = "newfoundHolder">

<img src="gui/assets/Newfound Knowledge.png" class = "newfound">
<div class = "titlefont"><div class = "newfoundtitle"> Newfound Knowledge </div> </div>

<div class = "newfoundContent">
  <img src="gui/assets/Newfound Border.png" class = "newfoundBorder">
  <img src="gui/assets/Placeholder.png" class = "placeholder" id = "newfoundPic">
  <div class = "newfoundText"> This is where the newfound knowledge facts will go hopefully, not really sure how this part will work though</div>

  <img src="gui/assets/LA1.png" class = "LA">
  <img src="gui/assets/RA1.png" class = "RA">
</div>
<img src="gui/assets/add1.png" class = "add">


<img src="gui/assets/Newfound-Animation.png" class="animationBlock">
</div>



</div>

<div class="exp">

    <div class = "exptitle"> Experience </div>

    <img src="gui/assets/Experience.png" class = "experience">

    <canvas id="canvas" width="600" height="600" style="border:1px solid #000000;" data-url="[{&quot;id&quot;:13,&quot;first_name&quot;:&quot;Bill &quot;,&quot;last_name&quot;:&quot;Nye&quot;,&quot;email&quot;:&quot;gasp@guy.com&quot;,&quot;exp&quot;:5110,&quot;password&quot;:&quot;jlasfasdfa&quot;,&quot;total_lecture_time&quot;:10,&quot;created_at&quot;:&quot;2015-08-07T19:37:08.651Z&quot;,&quot;updated_at&quot;:&quot;2015-08-07T19:37:20.611Z&quot;,&quot;level&quot;:&quot;Master&quot;},{&quot;id&quot;:14,&quot;first_name&quot;:&quot;jame&quot;,&quot;last_name&quot;:&quot;doe&quot;,&quot;email&quot;:&quot;Whatever@nonsense.com&quot;,&quot;exp&quot;:1500,&quot;password&quot;:&quot;sadflak&quot;,&quot;total_lecture_time&quot;:5,&quot;created_at&quot;:&quot;2015-08-07T19:37:57.779Z&quot;,&quot;updated_at&quot;:&quot;2015-08-07T19:38:06.405Z&quot;,&quot;level&quot;:&quot;Apprentice&quot;},{&quot;id&quot;:15,&quot;first_name&quot;:&quot;John&quot;,&quot;last_name&quot;:&quot;Watsone&quot;,&quot;email&quot;:&quot;Bluh@blank.com&quot;,&quot;exp&quot;:2055,&quot;password&quot;:&quot;SherlockROxs&quot;,&quot;total_lecture_time&quot;:5,&quot;created_at&quot;:&quot;2015-08-07T19:38:56.316Z&quot;,&quot;updated_at&quot;:&quot;2015-08-07T19:39:06.578Z&quot;,&quot;level&quot;:&quot;Journeyman&quot;},{&quot;id&quot;:16,&quot;first_name&quot;:&quot;Bill &quot;,&quot;last_name&quot;:&quot;Murphy&quot;,&quot;email&quot;:&quot;uhhhhh@nothing.com&quot;,&quot;exp&quot;:3610,&quot;password&quot;:&quot;fds;fsa&quot;,&quot;total_lecture_time&quot;:10,&quot;created_at&quot;:&quot;2015-08-07T19:51:19.226Z&quot;,&quot;updated_at&quot;:&quot;2015-08-07T19:51:28.392Z&quot;,&quot;level&quot;:&quot;Master&quot;},{&quot;id&quot;:17,&quot;first_name&quot;:&quot;new&quot;,&quot;last_name&quot;:&quot;person&quot;,&quot;email&quot;:&quot;dontcare@whatever.com&quot;,&quot;exp&quot;:3310,&quot;password&quot;:&quot;bluhbluh&quot;,&quot;total_lecture_time&quot;:10,&quot;created_at&quot;:&quot;2015-08-07T19:52:03.989Z&quot;,&quot;updated_at&quot;:&quot;2015-08-07T19:52:16.512Z&quot;,&quot;level&quot;:&quot;Expert&quot;},{&quot;id&quot;:19,&quot;first_name&quot;:&quot;John&quot;,&quot;last_name&quot;:&quot;Nye&quot;,&quot;email&quot;:&quot;d&quot;,&quot;exp&quot;:4800,&quot;password&quot;:&quot;fds;fsa&quot;,&quot;total_lecture_time&quot;:1,&quot;created_at&quot;:&quot;2015-08-07T21:01:24.538Z&quot;,&quot;updated_at&quot;:&quot;2015-08-07T21:06:40.259Z&quot;,&quot;level&quot;:&quot;Master&quot;}]" style="width: 600px; height: 600px;">
    stop using IE
    </canvas>

</div>

<div class="newfoundInput">

  <img src="gui/assets/Newfound Border.png" class = "newfoundBorder2">
  <img src="gui/assets/Placeholder.png" class = "placeholder" id = "myPic2">

  <textarea class = "newfoundFact"></textarea>
  <div class="submit">Submit</div>
  <div class = "newfoundPrompt">Enter your knowledge below</div>
</div>



</div>

<div class = "info">

<table class = "userInfo">
  <thead>
    <tr>
      <th>First name</th>
      <th>Last name</th>
      <th>Email</th>
      <th>Exp</th>
      <th>Level</th>
      <th>Employee of the Week</th>
      <th colspan="3">Options</th>
    </tr>
  </thead>

  <tbody>
      <tr>
        <td>Jacob</td>
        <td>Parpart</td>
        <td>gasp@guy.com</td>
        <td>5110</td>
        <td>Expert</td>
        <td>No</td>
        <td><a href="/users/13">Show</a></td>
        <td><a href="/users/13/edit">Edit</a></td>
        <td><a data-confirm="Are you sure?" rel="nofollow" data-method="delete" href="/users/13">Destroy</a></td>
      </tr>
      <tr>
        <td>Zach</td>
        <td>Homen</td>
        <td>Whatever@nonsense.com</td>
        <td>4550</td>
        <td>Journeyman</td>
        <td>Yes</td>
        <td><a href="/users/14">Show</a></td>
        <td><a href="/users/14/edit">Edit</a></td>
        <td><a data-confirm="Are you sure?" rel="nofollow" data-method="delete" href="/users/14">Destroy</a></td>
      </tr>
      <tr>
        <td>Kendall</td>
        <td>Henery</td>
        <td>Bluh@blank.com</td>
        <td>2055</td>
        <td>Apprentice</td>
        <td>No</td>
        <td><a href="/users/15">Show</a></td>
        <td><a href="/users/15/edit">Edit</a></td>
        <td><a data-confirm="Are you sure?" rel="nofollow" data-method="delete" href="/users/15">Destroy</a></td>
      </tr>
      <tr>
        <td>Anna</td>
        <td>Murphy</td>
        <td>uhhhhh@nothing.com</td>
        <td>3610</td>
        <td>Journeyman</td>
        <td>No</td>
        <td><a href="/users/16">Show</a></td>
        <td><a href="/users/16/edit">Edit</a></td>
        <td><a data-confirm="Are you sure?" rel="nofollow" data-method="delete" href="/users/16">Destroy</a></td>
      </tr>
      <tr>
        <td>Madelyn</td>
        <td>McQuilliam</td>
        <td>dontcare@whatever.com</td>
        <td>3310</td>
        <td>Journeyman</td>
        <td>No</td>
        <td><a href="/users/17">Show</a></td>
        <td><a href="/users/17/edit">Edit</a></td>
        <td><a data-confirm="Are you sure?" rel="nofollow" data-method="delete" href="/users/17">Destroy</a></td>
      </tr>
      <tr>
        <td>Graham</td>
        <td>Founds</td>
        <td>d</td>
        <td>5200</td>
        <td>Expert</td>
        <td>No</td>
        <td><a href="/users/19">Show</a></td>
        <td><a href="/users/19/edit">Edit</a></td>
        <td><a data-confirm="Are you sure?" rel="nofollow" data-method="delete" href="/users/19">Destroy</a></td>
      </tr>
  </tbody>
</table>


<br>


<p id="notice"></p>

<p class = "firstName">
  Zach
</p>

<p class = "lastName">
  Homen
</p>

<p class = "myEmail">
  gasp@guy.com
</p>

<p class = "funFact">
  blah blah blah.
</p>

<p class = "myLevel">
  Apprentice
</p>

<p class = "myExp">
  4550
</p>

<p>
  <strong>Badges:</strong>
  </p><ul class="badges">
    <li>Ten Hours Captioned</li>
    <li>Ten Hours Transcribed</li>
  </ul>
<p></p>


<a href="/users/13/updates/new">Back</a>

</div>


</div>


</body></html>
