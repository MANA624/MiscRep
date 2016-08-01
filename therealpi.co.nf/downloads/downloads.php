<?php

session_start();

function boxPrint($title, $paragraph){
        echo 
                                '<article>
                                        <header>
                                                <h1>'.$title.'</h1>
                                        </header>
                                        <br/><p class="paragraph">'.$paragraph.'</p>
                                        <footer>
                                                <p>developed by Matthew Niemiec</p>
                                        </footer>
                                </article>';
}

?>


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html lang="en">
<head>
	<meta charset="utf-8"/>
	<title>Downloads</title>
	<link rel="stylesheet" href="../main.css">
        <link rel="stylesheet" href="downloads.css">
</head>
<body>
	<div id="mainWrapper">
		<?php include '../header.php';?>
		
		<div id="bodyDiv">
		
			<section id="mainSection">
                                <a href="/downloads/programs/WinAverager.7z" download="Averager.7z">
                                        <?php boxPrint('Averager (Windows)', 'This is a small application used to store and calculate grades based on weights that the
                                                user inputs. It also has other functionalities, such as extra credit, opening syllabi, 
                                                and storing separate classes. To use on any Windows machine, simply download, extract
                                                using 7-zip, click Installer.exe, and follow directions'); ?>
                                </a>
                                
                                <a href="/downloads/programs/AveragerLinux.7z" download="Averager.7z">
                                        <?php boxPrint('Averager (Linux)', 'This is a small application used to store and calculate grades based on weights that the
                                                user inputs. It also has other functionalities, such as extra credit, opening syllabi, 
                                                and storing separate classes. To use, extract using 7-zip, save in a preferred location,
                                                and run executable'); ?>
                                </a>
                                
                                <a href="/downloads/programs/Averager.7z" download="Averager.7z">
                                        <?php boxPrint('Averager (Source Release)', 'This is a small application used to store and calculate grades based on weights that the
                                                user inputs. It also has other functionalities, such as extra credit, opening syllabi, 
                                                and storing separate classes. To use, extract using 7-zip, save in a preferred location,
                                                and run using Python'); ?>
                                </a>
                                
                        </section>
			
			<?php isset($_SESSION['username']) ? include '../logout.php' : include '../login.php'; ?>
		
		</div>
		
		<footer id="footer">
			@Copyright therealpi 2016
		</footer>
	</div>
</body>
</html>