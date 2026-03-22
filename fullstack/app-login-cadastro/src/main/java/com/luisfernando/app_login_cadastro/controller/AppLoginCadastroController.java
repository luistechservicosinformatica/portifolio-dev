package com.luisfernando.app_login_cadastro.controller;

import com.luisfernando.app_login_cadastro.services.CookieService;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.ui.Model;
import com.luisfernando.app_login_cadastro.model.User;
import com.luisfernando.app_login_cadastro.repository.AppLoginCadastroRepository;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.io.UnsupportedEncodingException;

@Controller
public class AppLoginCadastroController {

    private final BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();

    @Autowired
    private AppLoginCadastroRepository repository;

    @GetMapping("/")
    public String panel(Model model, HttpServletRequest request) throws UnsupportedEncodingException {
        String userId = CookieService.getCookie(request, "userId");

        if (userId == null) {
            return "redirect:/login";
        }

        model.addAttribute("id", CookieService.getCookie(request, "userId"));
        model.addAttribute("name", CookieService.getCookie(request, "userName"));

        return "index";
    }

    @GetMapping("/login")
    public String login(HttpServletRequest request) throws UnsupportedEncodingException {
        if (CookieService.getCookie(request, "userId") != null) {
            return "redirect:/";
        }
        return "login";
    }

    @PostMapping("/logar")
    public String userLogin(User user, HttpServletResponse response, RedirectAttributes redirect) throws UnsupportedEncodingException {
        User loginedUser = repository.findByEmail(user.getEmail());

        if (loginedUser == null || !encoder.matches(user.getPassword(), loginedUser.getPassword())) {
            redirect.addFlashAttribute("erro", "E-mail ou senha incorretos!");
            return "redirect:/login";
        }

        CookieService.setCookie(response, "userId", String.valueOf(loginedUser.getId()), 18000);
        CookieService.setCookie(response, "userName", loginedUser.getName(), 18000);
        return "redirect:/";
    }

    @GetMapping("/logar")
    public String logar() {
        return "redirect:/login";
    }

    @GetMapping("/logout")
    public String logout(HttpServletResponse response) throws UnsupportedEncodingException {
        CookieService.setCookie(response, "userId", "", 0);
        return "redirect:/login";
    }

    //------------------------CADASTRO---------------------------------------

    @GetMapping("/cadastro")
    public String signup(HttpServletRequest request) throws UnsupportedEncodingException {
        String userId = CookieService.getCookie(request, "userId");

        if (userId != null && !userId.isEmpty()) {
            return "redirect:/";
        }

        return "signup";
    }

    @PostMapping("/cadastro")
    public String userSignup(@Valid User user, BindingResult result, RedirectAttributes redirect, HttpServletRequest request) throws UnsupportedEncodingException {
        if (CookieService.getCookie(request, "userId") != null) {
            return "redirect:/";
        }

        if (result.hasErrors()) {
            redirect.addFlashAttribute("erro", "Dados inválidos");
            return "redirect:/cadastro";
        }

        if (repository.findByEmail(user.getEmail()) != null) {
            redirect.addFlashAttribute("erro", "Usuário já existente");
            return "redirect:/cadastro";
        }

        user.setPassword(encoder.encode(user.getPassword()));
        repository.save(user);

        redirect.addFlashAttribute("sucesso", "Cadastro realizado com sucesso");
        return "redirect:/login";
    }
}




