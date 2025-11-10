import 'package:flutter/material.dart';

class FormularyScreen extends StatefulWidget {
  const FormularyScreen({super.key});

  @override
  State<FormularyScreen> createState() => _FormularyScreenState();
}

class _FormularyScreenState extends State<FormularyScreen> {
  final _search = TextEditingController();

  //dummy data
  final List<Map<String, String>> _drugs = [
    {
      'id': 'DR-001',
      'brand_name': 'Biogesic',
      'generic_name': 'Paracetamol',
      'dosage_form': 'Tablet',
      'drug_strength': '500 mg',
      'drug_category': 'Analgesic',
    },
    {
      'id': 'DR-002',
      'brand_name': 'Alnix',
      'generic_name': 'Cetirizine Hydrochloride',
      'dosage_form': 'Syrup',
      'drug_strength': '5 mg',
      'drug_category': 'Antihistamine',
    },
    {
      'id': 'DR-003',
      'brand_name': 'Amoxil',
      'generic_name': 'Amoxicillin',
      'dosage_form': 'Capsule',
      'drug_strength': '500 mg',
      'drug_category': 'Antibiotic',
    },
  ];

  String _ls(Object? v) => (v ?? "").toString().toLowerCase();

  @override
  Widget build(BuildContext context) {
    final kw = _ls(_search.text);

    final filtered = _drugs.where((d) {
      if (kw.isEmpty) return true;
      return _ls(d['id']).contains(kw) ||
          _ls(d['brand_name']).contains(kw) ||
          _ls(d['generic_name']).contains(kw);
    }).toList();

    return Container(
      padding: const EdgeInsets.all(22),
      color: const Color(0xFFF1F4F2),
      child: Center(
        child: Container(
          width: double.infinity,
          constraints: const BoxConstraints(
            maxWidth: 1100,
            minHeight: 780, 
          ),
          padding: const EdgeInsets.all(22),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(12),
            boxShadow: const [
              BoxShadow(color: Colors.black12, blurRadius: 6, offset: Offset(0, 2)),
            ],
          ),

          child: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  "Formulary",
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.w700),
                ),

                const SizedBox(height: 20),

                Row(
                  children: [
                    const Spacer(),

                    SizedBox(
                      width: 340,
                      child: TextField(
                        controller: _search,
                        decoration: InputDecoration(
                          hintText: 'Search Drug ID or Name',
                          prefixIcon: const Icon(Icons.search),
                          filled: true,
                          fillColor: Colors.white,
                          contentPadding:
                              const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(10),
                            borderSide: const BorderSide(color: Color(0xFFE0E0E0)),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(10),
                            borderSide: const BorderSide(color: Color(0xFFE0E0E0)),
                          ),
                          focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(10),
                            borderSide: BorderSide(
                              color: const Color(0xFF34933B),
                              width: 1.8,
                            ),
                          ),
                        ),
                        onChanged: (_) => setState(() {}),
                      ),
                    ),

                    const SizedBox(width: 10),

                    Container(
                      height: 44,
                      width: 44,
                      decoration: const BoxDecoration(
                        color: Color(0xFF34933B),
                        shape: BoxShape.circle,
                      ),
                      child: IconButton(
                        icon: const Icon(Icons.search, color: Colors.white),
                        onPressed: () => setState(() {}),
                      ),
                    )
                  ],
                ),

                const SizedBox(height: 20),

                ClipRRect(
                  borderRadius: BorderRadius.circular(8),
                  child: Container(
                    width: double.infinity,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      border: Border.all(color: const Color(0xFFE0E0E0)),
                    ),
                    child: DataTable(
                      columnSpacing: 28,
                      headingRowHeight: 48,
                      dataRowMinHeight: 48,
                      dataRowMaxHeight: 56,
                      headingRowColor:
                          MaterialStatePropertyAll(Colors.grey.shade100),

                      columns: const [
                        DataColumn(
                            label: Text('Drug ID',
                                style: TextStyle(fontWeight: FontWeight.bold))),
                        DataColumn(
                            label: Text('Brand Name',
                                style: TextStyle(fontWeight: FontWeight.bold))),
                        DataColumn(
                            label: Text('Generic Name',
                                style: TextStyle(fontWeight: FontWeight.bold))),
                        DataColumn(
                            label: Text('Form',
                                style: TextStyle(fontWeight: FontWeight.bold))),
                        DataColumn(
                            label: Text('Strength',
                                style: TextStyle(fontWeight: FontWeight.bold))),
                        DataColumn(
                            label: Text('Category',
                                style: TextStyle(fontWeight: FontWeight.bold))),
                      ],

                      rows: [
                        for (final d in filtered)
                          DataRow(
                            cells: [
                              DataCell(Text(d['id']!)),
                              DataCell(Text(d['brand_name']!)),
                              DataCell(Text(d['generic_name']!)),
                              DataCell(Text(d['dosage_form']!)),
                              DataCell(Text(d['drug_strength']!)),
                              DataCell(Text(d['drug_category']!)),
                            ],
                          ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
