package com.luisfernando.app_login_cadastro.repository;

import com.luisfernando.app_login_cadastro.model.User;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

public interface AppLoginCadastroRepository extends CrudRepository<User, String> {

    User findById(Long id);
    User findByEmail(String email);

    @Query(value="SELECT * FROM user WHERE email = :email AND password = :password", nativeQuery = true)
    public User login(String email, String password);

}
