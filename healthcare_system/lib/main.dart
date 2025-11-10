
import 'package:flutter/material.dart';
import 'screens/login_form.dart';
import 'screens/dashboard.dart';

void main() => runApp(const StBlaiseApp());

class StBlaiseApp extends StatelessWidget {
  const StBlaiseApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'St. Blaise Medical Clinic and Pharmacy',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorSchemeSeed: const Color(0xFF34933B), 
        inputDecorationTheme: const InputDecorationTheme(
          border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(10))),
          contentPadding: EdgeInsets.symmetric(horizontal: 14, vertical: 12),
        ),
      ),
      initialRoute: '/login',
      routes: {
        '/login': (_) => const LoginScreen(),
        '/dashboard': (_) => const DashboardScreen(),
      },
    );
  }
}










