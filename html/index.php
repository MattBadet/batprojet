<!DOCTYPE html>
<html lang="fr">
    <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="image/logo_BATprojet.jpg" />
    <title>BATprojet</title>
    <H1 class="txt">Bienvenue, sur la gestion des bidons de gel hydroalcoolique.</H1>
    <h1>
    <table>
        <tr><td><a href=index.php>Acceuil</a></td>
        <td><a href=plan.php></a>Plan des bonbonnes</a></td>
        <td><a href=page_type_bonbonne.php>Page type de bonbonne</a></td></tr>
    </table>
    </h1>
    </head>
    <body>
    <p class="txt">Vous pouvez vérifier le niveau des différentes bonbonnes ci-dessous.</p>
    <div id='bonbonne'>
        <table class="tabl_bidon"><tr><td>
        <p>Bidon n°1</p>
	<?php
		function read($csv){
            $file = fopen($csv, 'r');
            while (!feof($file) ) {
                $line[] = fgetcsv($file, 1024);
            }
            fclose($file);
            return $line;
        }
		$csv = 'bouteille.csv';
        $csv = read($csv);
		
                $a = $csv[1][3];
                if ($a < 100 || $a == 100) {
                    if( $a > 75)
                        echo '<img src="image/fiole_100.png"/>';}
                if ($a < 75 || $a == 75) {
                    if( $a > 50)
                        echo '<img src="image/fiole_75.png"/>';}
                if ($a < 50|| $a == 50) {
                    if( $a > 25)
                        echo '<img src="image/fiole_50.png"/>';}
                if ($a < 25|| $a == 25) {
                    if( $a > 5)
                        echo '<img src="image/fiole_25.png"/>';}
                if ($a < 5|| $a == 5) {
                    if( $a > 0 || $a == 0)
                        echo '<img src="image/fiole_5.png"/>';}
                
            ?>       
        <td><p class="invisble">Bidon n°x</td>
        <td><p>Bidon n°2</p>
        <?php 
                $a = $csv[2][3];
                if ($a < 100 || $a == 100) {
                    if( $a > 75)
                        echo '<img src="image/fiole_100.png"/>';}
                if ($a < 75 || $a == 75) {
                    if( $a > 50)
                        echo '<img src="image/fiole_75.png"/>';}
                if ($a < 50|| $a == 50) {
                    if( $a > 25)
                        echo '<img src="image/fiole_50.png"/>';}
                if ($a < 25|| $a == 25) {
                    if( $a > 5)
                        echo '<img src="image/fiole_25.png"/>';}
                if ($a < 5|| $a == 5) {
                    if( $a > 0 || $a == 0)
                        echo '<img src="image/fiole_5.png"/>';}
                
            ?>   
        <tr><td><p>Bidon n°3</p>
        <?php 
                $a = $csv[3][3];
                if ($a < 100 || $a == 100) {
                    if( $a > 75)
                        echo '<img src="image/fiole_100.png"/>';}
                if ($a < 75 || $a == 75) {
                    if( $a > 50)
                        echo '<img src="image/fiole_75.png"/>';}
                if ($a < 50|| $a == 50) {
                    if( $a > 25)
                        echo '<img src="image/fiole_50.png"/>';}
                if ($a < 25|| $a == 25) {
                    if( $a > 5)
                        echo '<img src="image/fiole_25.png"/>';}
                if ($a < 5|| $a == 5) {
                    if( $a > 0 || $a == 0)
                        echo '<img src="image/fiole_5.png"/>';}
                
            ?>   
        <td><p class="invisble">Bidon n°x</td>
        <td><p>Bidon n°4</p>
        <?php 
                $a = $csv[4][3];
                if ($a < 100 || $a == 100) {
                    if( $a > 75)
                        echo '<img src="image/fiole_100.png"/>';}
                if ($a < 75 || $a == 75) {
                    if( $a > 50)
                        echo '<img src="image/fiole_75.png"/>';}
                if ($a < 50|| $a == 50) {
                    if( $a > 25)
                        echo '<img src="image/fiole_50.png"/>';}
                if ($a < 25|| $a == 25) {
                    if( $a > 5)
                        echo '<img src="image/fiole_25.png"/>';}
                if ($a < 5|| $a == 5) {
                    if( $a > 0 || $a == 0)
                        echo '<img src="image/fiole_5.png"/>';}
                
            ?>  
        </table>
        </div>
    </body>
    <script>
        setInterval('load_value()', 2000);
        function load_value(){
            $('#bonbonne').load('load_bonbonne.php');
        }
    </script>
    <bottom class="bott">
        <p>Chérie, Sa va couper couper !</p>
    </bottom>
</html>





