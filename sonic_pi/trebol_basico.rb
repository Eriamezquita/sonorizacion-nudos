# Sonificación básica del nudo trébol en Sonic Pi
# Idea: cierre conceptual de la trenza sigma_1^3 → tres eventos ascendentes.

use_bpm 90

braid_word = [1, 1, 1]
base_note = 57 # A3

live_loop :trebol do
  braid_word.each do |generator|
    if generator > 0
      play base_note + 2 * generator, release: 0.25, amp: 0.8
    elsif generator < 0
      play base_note + 2 * generator, release: 0.25, amp: 0.8
    else
      sleep 0.25
    end
    sleep 0.5
  end
  sleep 1
end
