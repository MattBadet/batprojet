<div id="global">
    <div id="gauche">
        <a href=bonbonne_1.html><p>Bidon n°1</p>
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
                
        ?></a>

        <a href=bonbonne_3.html><p>Bidon n°3</p>
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
            
        ?></a>
    </div>

    <div id="droit">
        <a href=bonbonne_2.html><p>Bidon n°2</p>
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
            
        ?></a>
        
        <a href=page_type_bonbonne.html><p>Bidon n°4</p>
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
            
        ?></a>
    </div>
</div>