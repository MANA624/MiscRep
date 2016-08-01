<?php

session_start();

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html lang="en">
<head>
	<meta charset="utf-8"/>
	<title>About</title>
	<link rel="stylesheet" href="../main.css">
</head>
<body>
	<div id="mainWrapper">
		<?php include '../header.php';?>
		
		<div id="bodyDiv">
		
			<section id="mainSection">
				<article>
					<header>
						<hgroup>
							<h1>This is a little section about ME!</h1>
						</hgroup>
					</header>
					<p>So keep your prying eyes off</p>
					<footer>
						<p>wzritten by Matthew Niemiec</p>
					</footer>
				</article>
			</section>
			
			<?php isset($_SESSION['username']) ? include '../logout.php' : include '../login.php'; ?>
		
		</div>
		
		<footer id="footer">
			@Copyright therealpi 2016
		</footer>
	</div>
</body>
</html>