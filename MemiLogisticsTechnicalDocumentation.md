# Memi Logistics Platform

## Technical Documentation

### 1. Platform Overview
The platform serves as a digital logistics(freight) brokerage and fleet management ecosystem. It bridges the gap between Shippers (entities with goods) and Carriers (entities with transport capacity) through automated matching, real-time visibility, and end-to-end shipment lifecycle management. The platform leverages a decoupled microservices architecture to handle real-time GPS telemetry, automated load matching, and end-to-end shipment lifecycles.

---

### 2. Core Feature Modules

#### A. Smart Matching Engine
The heart of the platform uses multi-variable logic to ensure the right vehicle is assigned to the right load.
- **Geospatial Routing**: Matches loads to carriers based on proximity to the pickup point to minimize "deadhead" miles.
- **Capacity Filtering**: Filters by vehicle type and weight/volume constraints.
- **Requirements Mapping**: Matches specialized shipment needs (e.g. hazardous materials, temperature-controlled) with certified carriers.

#### B. Real-Time Execution & Visibility
- **GPS Telemetry**: Live tracking of the vehicle's position during active duty, integrated via mobile app or hardware devices.
- **Status Management**: Automated milestones (Dispatched → At Pickup → In Transit → At Delivery → Completed).
- **Instant Messaging**: Secure, in-app communication channel between the shipper and the driver and/or the company to handle exceptions without leaving the platform.

#### C. Digital Documentation & Finance
- **e-BOL & e-POD**: Digital Bill of Lading and Proof of Delivery (with photo/signature capture) to trigger instant invoicing.
- **Automated Invoicing**: System-generated billing based on agreed rates and logged detention times.

---

### 3. Recommended Advanced Features
To stay competitive globally, we recommended the following modules for future integration:
- **Dynamic Pricing AI**: A tool that suggests market-reflective rates based on seasonal demand, fuel prices, and historical data.
- **Predictive ETA**: Machine learning models that account for traffic, weather, and border crossing delays to provide more accurate delivery windows.
- **Fuel & Expense Monitoring**: Integration with fuel cards or hardware sensors to monitor consumption and detect fuel theft/drainage.
- **Carrier Scorecards**: A rating system based on punctuality, cargo safety, and communication quality.

---

### 4. Operational Workflow

| Operation        | Action                                           | Responsible Party |
|------------------|--------------------------------------------------|-------------------|
| Load Posting     | Inputting cargo details, dimensions, and destination. | Shipper           |
| Bidding/Matching | Platform identifies eligible carriers; carriers bid or "Order Shipment Now." | System / Carrier |
| Dispatch         | Assignment confirmed; digital paperwork generated. | Carrier           |
| Transit          | Live GPS tracking and real-time status updates enabled. | Driver / System  |
| Delivery         | Receiver signs e-POD via mobile app or web.       | Driver            |
| Settlement       | Automated invoice generation and payment processing. | System           |

---

### 5. Technical Architecture

#### Domain-Driven Design (DDD) Structure
The system is partitioned into **Bounded Contexts**, ensuring that each logistical function has its own logic, data schema, and clear boundaries.

**Core Bounded Contexts**
- Shipping Context
- Carrier Context
- Matching Context
- Tracking Context
- Financial Context
- Document Context
- Auth Context (Identity & Access)
- Notification Context
- Exception (Incident) Context
- Analytics & Reporting Context
- Routing / Optimization Context

#### Tactical Design Patterns
- **Aggregates**: Shipment, Carrier, Assignment, Invoice, Payment, User
- **Value Objects**: Address, Money, GPSCoordinates, Weight, Volume, Dimensions, TimeWindow, DriverLicense, DocumentReference
- **Domain Services**: RouteOptimizer

---

### Core Aggregates & Business Invariants
- **Shipment Aggregate (Root: Shipment)**
  - Entities: Stops, StatusHistory, DigitalDocuments, AssignmentRef, PricingDetails
  - Invariants: Cannot transition from Delivered back to In Transit, must have CarrierID before Dispatched, etc.

- **Carrier Aggregate (Root: Carrier)**
  - Entities: Vehicles, Drivers, ComplianceDocs, AvailabilitySchedule, CurrentAssignments
  - Invariants: Driver license validity, vehicle capacity ≥ load weight, valid insurance required, etc.

- **Financial Aggregate (Root: Invoice / Payment)**
  - Entities: Invoice, Payment, LineItems, Charges
  - Invariants: Invoice total must equal sum of line items, payment cannot exceed invoice amount, etc.

- **Document Aggregate (Root: DocumentBundle or ShipmentDocuments)**
  - Entities: BOL, POD, Attachments
  - Invariants: POD must include signature/photo, BOL must exist before dispatch, etc.

- **Tracking Aggregate (Root: TrackingSession)**
  - Entities: LocationPoints, Route, GeofenceZones
  - Invariants: Location timestamps strictly increasing, GPS coordinates valid, etc.

- **Assignment Aggregate (Root: Assignment)**
  - Entities: ShipmentID, CarrierID, DriverID, VehicleID
  - Invariants: One active assignment per shipment, driver/vehicle cannot be double-assigned, etc.

- **Rating / Scorecard Aggregate (Root: CarrierScore)**
  - Entities: Ratings, Reviews, Metrics
  - Invariants: Rating range 1–5, one rating per shipment per shipper, etc.

---

### Event-Driven Architecture (EDA)
The platform operates on an asynchronous **Publish-Subscribe** model using Kafka/RabbitMQ.

**Event Pipeline**
1. Event Producers: Driver App, Shipper Portal, IoT sensors
2. Message Broker: Routes events
3. Event Consumers: Notification Service, Analytics Service, Billing Service

**Key Domain Events**
- Shipment Lifecycle Events (LoadCreated, CarrierMatched, ShipmentPickedUp, etc.)
- Carrier & Matching Events (CarrierRequested, CarrierAccepted, MatchingFailed, etc.)
- Tracking & Geofence Events (ArrivedAtPickup, GeofenceBreached, etc.)
- Financial Events (InvoiceGenerated, PaymentCompleted, etc.)
- Document Events (BOLGenerated, PODUploaded, etc.)
- Exception & Risk Events (ShipmentAtRisk, IncidentReported, etc.)
- User & Security Events (UserRegistered, UnauthorizedAccessAttempted, etc.)
- AI / Optimization Events (ETAUpdated, RouteOptimized, etc.)
- System-Level Events (ServiceDegraded, RetryTriggered, etc.)

---

### 6. Backend Infrastructure & Scalability

#### A. API & Security Model
- JWT-based Authentication
- Role-Based Access Control (RBAC)
- Roles: SHIPPER, CARRIER, DRIVER, ADMIN

#### B. Scalability & Resilience
- Horizontal Scaling via Kubernetes
- Strong Consistency for Financials, Eventual Consistency for Tracking
- Circuit Breakers, Idempotency

#### C. Observability
- Logging: ELK Stack
- Metrics: Prometheus & Grafana
- Tracing: OpenTelemetry
- Geofencing Service

---

### Frontend & Interface
- **Web Portal**: Responsive dashboard for shippers
- **Mobile Application**: Driver-centric app for GPS, documents, status
