package com.luisfernando.agendador_horarios.controller;

import com.luisfernando.agendador_horarios.infrastructure.entity.AgendamentoEntity;
import com.luisfernando.agendador_horarios.services.AgendamentoService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

@RestController
@RequestMapping("/agendamentos")
@RequiredArgsConstructor
public class AgendamentoController {

    private final AgendamentoService agendamentoService;

    @PostMapping
    public ResponseEntity<AgendamentoEntity> salvarAgendamento(@RequestBody AgendamentoEntity agendamento) {
        return ResponseEntity.status(201).body(agendamentoService.salvarAgendamento(agendamento));
    }

    @DeleteMapping
    public ResponseEntity<Void> deletarAgendamento(@RequestParam String cliente, @RequestParam LocalDateTime dataHoraAgendamento) {
        agendamentoService.deletarAgendamento(cliente, dataHoraAgendamento);
        return ResponseEntity.noContent().build();
    }

    @GetMapping
    public ResponseEntity<List<AgendamentoEntity>> listarAgendamentosDiarios(@RequestParam String profissional, @RequestParam LocalDate data) {
        return ResponseEntity.ok().body(agendamentoService.buscarAgendamentosDoDia(profissional, data));
    }

    @PutMapping
    public ResponseEntity<AgendamentoEntity> editarAgendamento(@RequestBody AgendamentoEntity agendamento, @RequestParam String cliente, @RequestParam LocalDateTime dataHoraAgendamento) {
        return ResponseEntity.ok().body(agendamentoService.editarAgendamento(agendamento, cliente, dataHoraAgendamento));          // ao invés do "ok()" pode ser o "accepted()", só muda o erro
    }

}
