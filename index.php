<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <title>Chat with Light System</title>
    <link type="text/css" rel="stylesheet" href="css/styles.css" />
</head>

<body>
        
    <div id = 'border'>
        
        <div id ='menu'>

            <p class = 'welcome'>welcome,<b></b></p>
            <p class="logout"><a id="exit" href="#">logout</a></p>
            <div style="clear:both"></div>
        
        </div>

        <div id="chatbox"></div>

        <form name="message" action="">

            <input name="UsrMsg" type="text" id="UsrMsg" size="63" />
            <input name="submitMsg" type="submit" id="submitMsg" value="Send" />
            
        </form>

    </div>

    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3/jquery.min.js"></script>

    <script type="text/javascript">

        $(document).ready(function(){

        })
        
    </script>

</body>

</html>