<?php
// ============================================================
// TAMARIU CHALET — Contact Form Mail Handler
// File: send-mail.php
// Upload to: root of your site (same level as index.html)
// ============================================================

// ── CONFIGURATION ──
$to         = 'tamariuchalet@gmail.com';
$from_email = 'noreply@tamariuchalet.com';
$from_name  = 'Tamariu Chalet Website';
$subject_prefix = 'Booking Enquiry';

// ── SECURITY: Only accept POST requests ──
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    die('Method not allowed');
}

// ── SECURITY: Check the request comes from your own site ──
$origin = isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : '';
if (strpos($origin, 'tamariuchalet.com') === false) {
    http_response_code(403);
    die('Forbidden');
}

// ── COLLECT & SANITISE FORM FIELDS ──
function clean($value) {
    return htmlspecialchars(strip_tags(trim($value)), ENT_QUOTES, 'UTF-8');
}

$name     = clean($_POST['name']     ?? '');
$email    = clean($_POST['email']    ?? '');
$phone    = clean($_POST['phone']    ?? '');
$room     = clean($_POST['room']     ?? '');
$checkin  = clean($_POST['checkin']  ?? '');
$checkout = clean($_POST['checkout'] ?? '');
$guests   = clean($_POST['guests']   ?? '');
$cost     = clean($_POST['cost']     ?? '');
$message  = clean($_POST['message']  ?? '');

// ── VALIDATE required fields ──
$errors = [];
if (empty($name))     $errors[] = 'Name is required';
if (empty($email))    $errors[] = 'Email is required';
if (!filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) $errors[] = 'Invalid email address';
if (empty($room))     $errors[] = 'Please select a room';
if (empty($checkin))  $errors[] = 'Check-in date is required';
if (empty($checkout)) $errors[] = 'Check-out date is required';

if (!empty($errors)) {
    http_response_code(400);
    header('Content-Type: application/json');
    echo json_encode(['success' => false, 'errors' => $errors]);
    exit;
}

// ── BUILD EMAIL ──
$subject = "{$subject_prefix} — {$room} — {$checkin} to {$checkout}";

$body = "
NEW BOOKING ENQUIRY — TAMARIU CHALET
=====================================

GUEST DETAILS
-------------
Name:    {$name}
Email:   {$email}
Phone:   {$phone}
Guests:  {$guests}

BOOKING DETAILS
---------------
Room:           {$room}
Check-in:       {$checkin}
Check-out:      {$checkout}
Estimated Cost: {$cost}

MESSAGE
-------
{$message}

=====================================
Sent from tamariuchalet.com
";

// ── MAIL HEADERS ──
$headers  = "From: {$from_name} <{$from_email}>\r\n";
$headers .= "Reply-To: {$name} <{$_POST['email']}>\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";

// ── SEND ──
$sent = mail($to, $subject, $body, $headers);

// ── RESPOND ──
header('Content-Type: application/json');
if ($sent) {
    echo json_encode(['success' => true]);
} else {
    http_response_code(500);
    echo json_encode(['success' => false, 'errors' => ['Mail server error — please email us directly at tamariuchalet@gmail.com']]);
}
?>
