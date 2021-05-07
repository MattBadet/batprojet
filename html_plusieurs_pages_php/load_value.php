<div id="global">
    <div id="gauche">
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
    </div>
    <div id="droit">
        <p>Bonbonne n°X du batiment F</p>
        <?php
        $pc = $csv[1][3];
        echo "<p>Niveau de la bonbonne : ${pc}%</p>" ;
        ?>
        <img src="image/bidon_X_bat_x.png" class="larg">
    </div>
</div>