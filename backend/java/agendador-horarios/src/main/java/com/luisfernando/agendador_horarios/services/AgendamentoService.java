package com.luisfernando.agendador_horarios.services;

import com.luisfernando.agendador_horarios.infrastructure.entity.AgendamentoEntity;
import com.luisfernando.agendador_horarios.infrastructure.repository.AgendamentoRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Objects;

@Service
@RequiredArgsConstructor  // injeção de dependencia
public class AgendamentoService {

    private final AgendamentoRepository agendamentoRepository;

    public AgendamentoEntity salvarAgendamento(AgendamentoEntity agendamento) {
        LocalDateTime horaAgendamento = agendamento.getDataHoraAgendamento();
        LocalDateTime horaFim = agendamento.getDataHoraAgendamento().plusHours(1);

        AgendamentoEntity agenda = agendamentoRepository.findByServicoAndDataHoraAgendamentoBetween(agendamento.getServico(), horaAgendamento, horaFim);

        if  (Objects.nonNull(agenda)) {
            throw new IllegalArgumentException("Horário ocupado");
        }

        return agendamentoRepository.save(agendamento);      // cometi um erro aqui, coloquei "agenda"
    }

    public void deletarAgendamento(String cliente, LocalDateTime dataHoraAgendamento) {
        agendamentoRepository.deleteByClienteAndDataHoraAgendamento(cliente, dataHoraAgendamento);
    }

    public List<AgendamentoEntity> buscarAgendamentosDoDia(String profissional, LocalDate data) {
        LocalDateTime primeiraHoraDoDia = data.atStartOfDay();
        LocalDateTime ultimaHoraDoDia = data.atTime(23, 59, 59);

        return agendamentoRepository.findByProfissionalAndDataHoraAgendamentoBetween(profissional, primeiraHoraDoDia, ultimaHoraDoDia);
    }

    public AgendamentoEntity editarAgendamento(AgendamentoEntity agendamento, String cliente, LocalDateTime dataHoraAgendamento) {
        AgendamentoEntity agenda = agendamentoRepository.findByClienteAndDataHoraAgendamento(cliente, dataHoraAgendamento);

        if  (Objects.isNull(agenda)) {
            throw new IllegalArgumentException("Horário ocupado");
        }

        agendamento.setId(agenda.getId());
        return agendamentoRepository.save(agendamento);   // cometi um erro aqui, coloquei "agenda"
    }

}
