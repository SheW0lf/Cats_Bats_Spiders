<?php
    /**
     * Author: Damian Dabrowski
     * Language: PHP
     * Github: https://github.com/ddcodepl
     */

    $elements = [];
    for ($i = 1; $i <= 100; $i++) {
        if ($i % 3 === 0) {
            if ($i % 5 === 0) {
                $elements[$i] = "Spiders ";
            } else {
                $elements[$i] = "Cats ";
            }
        } else if ($i % 5 === 0) {
            $elements[$i] = "Bats ";
        } else {
            $elements[$i] = "$i ";
        }
    }

    print_r($elements);