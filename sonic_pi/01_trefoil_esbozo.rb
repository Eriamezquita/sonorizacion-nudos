# Sonorización de nudos
# Prototipo 01: nudo trébol
#
# Este archivo no pretende ser todavía una sonificación matemática completa.
# Es un primer boceto audible: tres cruces, repetición, variación y registro.

use_bpm 72

# Tres eventos como analogía inicial del nudo trébol.
# +1 puede leerse como cruce positivo; -1 como cruce negativo.
cruces = [1, 1, 1]

# Escala inicial: puede cambiarse según el carácter del experimento.
notas_base = [:c4, :e4, :g4]

define :tocar_cruce do |signo, nota, duracion|
  if signo > 0
    synth :piano
    play nota, amp: 0.9, sustain: duracion * 0.5
  else
    synth :dark_ambience
    play note(note) - 12, amp: 0.6, sustain: duracion
  end
  sleep duracion
end

live_loop :trebol_piano do
  cruces.each_with_index do |c, i|
    tocar_cruce c, notas_base[i], 0.5
  end

  # Pequeña variación: el motivo se deforma sin perder identidad.
  play_pattern_timed [:c5, :g4, :e4], [0.25, 0.25, 0.5], amp: 0.55
end

live_loop :pulso_bajo do
  sync :trebol_piano
  synth :fm
  play :c2, sustain: 1.5, amp: 0.45
  sleep 2
end
