<?php include 'counting.php'; 

session_start();

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html lang="en">
<head>
	<meta charset="utf-8">
        <meta name="Description" content="The Real Pi">
        <meta name="keywords" content="Downloads, Projects, Internhsip, Employer">
        <meta name="Author" content="Matthew Niemiec">
	<title>Welcome to The Real Pi!</title>
        <script src="prefixfree.js"></script>
	<link rel="stylesheet" href="main.css" />
        <link rel="shortcut icon" href="favicon.ico" type="favicon/ico" />
</head>
<body>
	<div id="mainWrapper">
	<?php include 'header.php';?>
		<div id="bodyDiv">
		
			<section id="mainSection">
				<article>
					<header>
						<hgroup>
							<h1>What is The Real Pi?</h1>
						</hgroup>
					</header>
                                                <br/><p class="paragraph">The Real Pi is a privately developed site soley intended for personal use. The main purpose
                                                of the site is to post projects for other people to use, and so for that purpose, there
                                                will always be source code and executables as necessary for each program developed. If 
                                                you are a potential employer, then I greatly appreciate your consideration and hope that
                                                you will take the time to log in using the user name and password given on my résumé and 
                                                look at the special back-end code and features. To all reading, If you have any comments or 
                                                suggestions, please feel free to leave an email in the Contact Us section. Again, thank
                                                you for your interest and hope you enjoy The Real Pi.<br/>
                                                </p>
					<footer>
						<p>written by Matthew Niemiec</p>
					</footer>
				</article>
			</section>
			
                        <?php isset($_SESSION['username']) ? include 'logout.php' : include 'login.php'; ?>
		
		</div>
		
		<footer id="footer">
			@Copyright therealpi 2016
                        
		</footer>
	</div>
</body>
</html>