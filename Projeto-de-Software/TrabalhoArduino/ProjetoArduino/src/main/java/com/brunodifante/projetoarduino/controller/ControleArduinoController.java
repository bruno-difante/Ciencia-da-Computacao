package com.brunodifante.projetoarduino.controller;

import com.brunodifante.projetoarduino.model.Led;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/")
public class ControleArduinoController {

    private final Led led = new Led("COM5", 9600); // Porta do Arduino

    @GetMapping
    public String paginaInicial(Model model) {
        model.addAttribute("ligado", led.isLigado());
        return "index"; // index.html em src/main/resources/templates/
    }

    @PostMapping("/ligar")
    @ResponseBody
    public String ligarLuz() {
        led.ligar();
        return "Ligado";
    }

    @PostMapping("/desligar")
    @ResponseBody
    public String desligarLuz() {
        led.desligar();
        return "Desligado";
    }

    @PostMapping("/toggle")
    @ResponseBody
    public String alternarLuz() {
        led.alternar();
        return led.isLigado() ? "Ligado" : "Desligado";
    }
}
