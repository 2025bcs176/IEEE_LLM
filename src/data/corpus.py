"""Sample IFMIF-DONES domain corpus, evaluation queries and relevance judgements."""

CORPUS = [
# ---- answer-bearing passages (ground truth) ----
{"id": "doc_003", "text": "Fusion for Energy (F4E) is the European Union organisation that coordinates the European contribution to the construction of the IFMIF-DONES facility in Granada, Spain, on behalf of Euratom."},
{"id": "doc_018", "text": "The continuous liquid target loop uses liquid lithium to generate the high neutron flux; lithium flows as a free jet across the beam footprint."},
{"id": "doc_029", "text": "The liquid lithium jet is designed to flow at approximately 15 m/s at the beam interaction zone to ensure adequate heat removal and target stability."},
{"id": "doc_034", "text": "The deuteron beam strikes the flowing lithium target with a rectangular footprint of about 200 mm by 50 mm."},
{"id": "doc_042", "text": "The IFMIF-DONES accelerator is designed for a nominal deuteron beam energy of 40 MeV at a beam current of 125 mA."},
{"id": "doc_049", "text": "The Radio Frequency Quadrupole (RFQ) in the injector section operates at a radio frequency of 175 MHz."},
{"id": "doc_055", "text": "The superconducting radio-frequency (SRF) linear accelerator requires a beam current of 125 mA for full-power operation."},
{"id": "doc_061", "text": "The main acceleration cryomodules employ half-wave resonator (HWR) superconducting cavities operating at 175 MHz."},
{"id": "doc_077", "text": "Vacuum pressure in the beamline is maintained at 1e-7 mbar using turbo-molecular pumps and cryogenic pumps."},
{"id": "doc_081", "text": "Beam loss is mitigated by a low-loss lattice, collimators and beam diagnostics to prevent excessive activation of the beam pipe."},
{"id": "doc_088", "text": "The DONES neutron energy spectrum peaks around 14 MeV and is tailored to match the first-wall spectrum of the DEMO fusion reactor for fusion materials testing."},
{"id": "doc_093", "text": "Material samples in the High Flux Test Module (HFTM) are actively cooled by helium gas flowing through channels in the specimen holder."},
{"id": "doc_112", "text": "Boiling of liquid lithium is prevented by maintaining high flow velocity and pressure, keeping lithium subcooled as it absorbs the 5 MW beam power."},
{"id": "doc_115", "text": "Tested reduced-activation steel samples are expected to reach about 20 displacements per atom (dpa) per year in the high-flux region."},
{"id": "doc_122", "text": "The lithium target structural support (backplate) is engineered for an operational cycle of 11 months before dpa-induced embrittlement necessitates component swap."},
{"id": "doc_137", "text": "Impurities such as nitrogen and oxygen are removed from the lithium inventory by cold trapping and gettering with yttrium."},
{"id": "doc_142", "text": "Diagnostics monitoring the liquid lithium free surface include laser-based thickness sensors and videometry for stability."},
{"id": "doc_158", "text": "First-phase testing prioritises Eurofer97 and F82H variants of reduced-activation ferritic/martensitic (RAFM) steels."},
{"id": "doc_184", "text": "Irradiated capsules are transferred from the test module to hot cells via a pneumatic rabbit system and shielded casks for post-irradiation examination."},
{"id": "doc_201", "text": "Safety containment protocols for tritium produced in the lithium loop include double confinement, tritium recovery systems and negative pressure gloveboxes."},
]

# Distractor passages (appended programmatically)
_distractors = [
("doc_010", "IFMIF-DONES is a particle accelerator facility under construction in Granada, Spain, for fusion materials testing."),
("doc_012", "The DEMO fusion reactor neutron spectrum is widely studied for plasma-facing components and breeding blankets."),
("doc_045", "Lithium-tritium reactions in the loop are analysed for tritium breeding and inventory control."),
("doc_100", "The accelerator injector includes an electron cyclotron resonance ion source producing deuterons."),
("doc_101", "Beam optics in the low-energy beam transport section focus the deuteron beam before the RFQ."),
("doc_102", "The medium-energy beam transport contains buncher cavities and quadrupole magnets."),
("doc_103", "Superconducting solenoids provide transverse focusing in the SRF linac cryomodules."),
("doc_104", "The high-energy beam transport delivers the beam to the lithium target with minimal loss."),
("doc_105", "Beam diagnostics include beam position monitors, profile monitors and Faraday cups."),
("doc_106", "The lithium loop includes a heat exchanger to remove the 5 MW deposited by the beam."),
("doc_107", "Cold traps in the lithium loop collect impurities by condensation at low temperature."),
("doc_108", "Yttrium getters chemically bind nitrogen and oxygen dissolved in liquid lithium."),
("doc_109", "The target backplate is made of a RAFM steel to withstand radiation damage."),
("doc_110", "Post-irradiation examination of samples is performed in hot cells with remote manipulators."),
("doc_111", "Material samples are encapsulated and placed in the high-flux region of the HFTM."),
("doc_113", "Neutron flux in DONES reaches about 1e18 n/m2/s in the high-flux test region."),
("doc_114", "The DEMO reactor requires materials to withstand up to 20 dpa per full-power year."),
("doc_116", "Eurofer97 is a reduced-activation ferritic-martensitic steel developed for fusion applications."),
("doc_117", "F82H is a Japanese reduced-activation ferritic-martensitic steel for fusion reactors."),
("doc_118", "Helium cooling in the HFTM provides efficient heat removal from specimens."),
]
for _d, _t in _distractors:
    CORPUS.append({"id": _d, "text": _t})

QUERIES = [
{"id": "q_01", "text": "What is the planned nominal operating energy of the deuteron beam in the IFMIF-DONES accelerator?"},
{"id": "q_02", "text": "Which material is utilized for the continuous liquid target loop to generate the neutron flux?"},
{"id": "q_03", "text": "What is the expected structural degradation rate, measured in displacements per atom (dpa) per year, for the tested steel samples?"},
{"id": "q_04", "text": "How does the neutron energy spectrum of DONES compare to the spectrum expected in the DEMO fusion reactor?"},
{"id": "q_05", "text": "What specific organization coordinates the European contribution to the IFMIF-DONES construction in Granada?"},
{"id": "q_06", "text": "What is the required beam current for the superconducting radio-frequency (SRF) linear accelerator?"},
{"id": "q_07", "text": "Which diagnostics are implemented to monitor the stability and thickness of the liquid lithium free surface?"},
{"id": "q_08", "text": "What are the safety containment protocols for managing the radioactive tritium produced within the lithium loop?"},
{"id": "q_09", "text": "How are the material samples actively cooled within the High Flux Test Module (HFTM)?"},
{"id": "q_10", "text": "What type of superconducting cavities are utilized in the main acceleration cryomodules?"},
{"id": "q_11", "text": "What is the rectangular footprint size of the deuteron beam as it strikes the flowing lithium target?"},
{"id": "q_12", "text": "How is the vacuum pressure maintained at the required 10^-7 mbar threshold within the beamline?"},
{"id": "q_13", "text": "What mechanism prevents the boiling of the liquid lithium as it absorbs the 5 MW beam power?"},
{"id": "q_14", "text": "Which specific variants of reduced-activation ferritic/martensitic (RAFM) steels are prioritized for the first testing phase?"},
{"id": "q_15", "text": "What is the expected flow velocity of the liquid lithium jet at the beam interaction zone?"},
{"id": "q_16", "text": "How will the irradiated material capsules be transported from the test module to the hot cells for post-irradiation examination?"},
{"id": "q_17", "text": "What RF frequency operates the Radio Frequency Quadrupole (RFQ) in the accelerator's injector section?"},
{"id": "q_18", "text": "What is the designed lifespan of the lithium target backplate before it requires replacement due to radiation damage?"},
{"id": "q_19", "text": "How does the accelerator system mitigate beam loss to prevent excessive activation of the beam pipe?"},
{"id": "q_20", "text": "What purification methods are used to extract impurities like nitrogen and oxygen from the circulating lithium inventory?"},
]

QRELS = {
"q_01": "doc_042", "q_02": "doc_018", "q_03": "doc_115", "q_04": "doc_088",
"q_05": "doc_003", "q_06": "doc_055", "q_07": "doc_142", "q_08": "doc_201",
"q_09": "doc_093", "q_10": "doc_061", "q_11": "doc_034", "q_12": "doc_077",
"q_13": "doc_112", "q_14": "doc_158", "q_15": "doc_029", "q_16": "doc_184",
"q_17": "doc_049", "q_18": "doc_122", "q_19": "doc_081", "q_20": "doc_137",
}
