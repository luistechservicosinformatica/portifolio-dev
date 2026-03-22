package com.luisfernando.app_login_cadastro.services.Autenticator;

import com.luisfernando.app_login_cadastro.services.CookieService;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

import java.io.IOException;

@Component
public class AppLoginCadastroInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws IOException {
        if (CookieService.getCookie(request, "userId") != null) {
            return true;
        }

        response.sendRedirect("/login");
        return false;
    }

}
