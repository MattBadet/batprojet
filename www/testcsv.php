<!DOCTYPE html>
<html lang="fr">
    <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="image/logo_BATprojet.jpg" />
    <title>BATprojet</title>
    <H1 class="txt">Bienvenue, sur la gestion des bidons de gel hydroalcoolique.</H1>
    </head>
    <body>
        <p class="txt">Vous pouvez vérifier le niveau des différentes bonbonnes ci-dessous.</p>
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
                // Définir le chemin d'accès au fichier CSV
                $csv = 'bouteille.csv';
                $csv = read($csv);
                echo '<pre>';
                print_r($csv);
                echo '</pre>';


                $a = $csv[1][2];
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
    </body>
    <bottom class="bott">
        <p>Chérie, Sa va couper couper !</p>
    </bottom>
</html>  