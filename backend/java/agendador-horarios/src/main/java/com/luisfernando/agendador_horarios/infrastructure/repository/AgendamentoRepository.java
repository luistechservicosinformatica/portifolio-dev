package com.luisfernando.agendador_horarios.infrastructure.repository;

import com.luisfernando.agendador_horarios.infrastructure.entity.AgendamentoEntity;
import jakarta.transaction.Transactional;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDateTime;
import java.util.List;

public interface AgendamentoRepository extends JpaRepository<AgendamentoEntity, Long> {

    AgendamentoEntity findByServicoAndDataHoraAgendamentoBetween(String servico, LocalDateTime dataHoraInicio, LocalDateTime dataHoraFim);

    @Transactional
    void deleteByClienteAndDataHoraAgendamento(String cliente, LocalDateTime dataHoraAgendamento);

    List<AgendamentoEntity> findByProfissionalAndDataHoraAgendamentoBetween(String profissional, LocalDateTime inicio, LocalDateTime fim);

    AgendamentoEntity findByClienteAndDataHoraAgendamento(String cliente, LocalDateTime dataHoraAgendamento);

}
