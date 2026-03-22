package com.luisfernando.app_login_cadastro.services;

import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.util.Arrays;
import java.util.Optional;

public class CookieService {

    public static void setCookie(HttpServletResponse response, String key, String value, int timer) throws UnsupportedEncodingException {
        String encodedValue = (value == null) ? "" : URLEncoder.encode(value, "UTF-8");

        Cookie cookie = new Cookie(key, encodedValue);
        cookie.setMaxAge(timer);
        cookie.setPath("/");
        cookie.setHttpOnly(true);
        // cookie.setSecure(true);      // Ative se usar HTTPS
        response.addCookie(cookie);
    }

    public static String getCookie(HttpServletRequest request, String key) throws UnsupportedEncodingException {
        String value = Optional.ofNullable(request.getCookies())
                .flatMap(cookies -> Arrays.stream(cookies)
                        .filter(cookie -> key.equals(cookie.getName()))
                        .findAny()
                ).map(Cookie::getValue) // abreviação de e -> e.getValue()
                .orElse(null);

        if (value != null) {
            return URLDecoder.decode(value, "UTF-8");
        }

        return null;
    }
}