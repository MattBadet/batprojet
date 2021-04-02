<!DOCTYPE html>
<html lang="fr">
    <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
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
        <H1>Bidon 1</H1>
        <div id = 'bonbonne'>
        <table>
            <tr><td>
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
            <td><table><tr><td><p>Bonbonne n°1 du batiment F</p></td></tr>"
            <?php
            $pc = $csv[1][3];
            echo "<tr><td><p>Niveau de la bonbonne : ${pc}%</p></td></tr>" ;
            ?>
            
            
            <tr><td><img src="image/bidon_X_bat_x.png" class="larg"></td></tr></table></td></tr>
        </table></div>
        <img src="image/plan_1.png" class="larg">
    </body>
    <script>
        setInterval('load_value()', 2000);
        function load_value(){
            $('#bonbonne').load('load_value.php');
        }
    </script>
    <bottom class="bott">
        <p>Ca va couper couper Chérie !</p>
    </bottom>
</html>
