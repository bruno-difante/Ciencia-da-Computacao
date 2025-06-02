package com.brunodifante.projetoarduino;

import com.brunodifante.projetoarduino.repository.ControlePorta;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ProjetoArduinoApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProjetoArduinoApplication.class, args);
        ControlePorta controle = new ControlePorta("COM5", 9600); // Substitua "COM3" pela sua porta COM

        // Enviar dados
        controle.enviaDados('1'); // Liga o LED
        try { Thread.sleep(100000); } catch (InterruptedException e) { e.printStackTrace(); }
        controle.enviaDados('2'); // Desliga o LED

        // Fechar a porta
        controle.close();
    }

}
